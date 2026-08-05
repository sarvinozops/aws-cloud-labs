# Load-Inventory Lambda function
#
# Triggered when an inventory CSV file is uploaded to Amazon S3.
# The function downloads the file and writes its records to DynamoDB.

import csv
import json
import urllib.parse

import boto3


s3 = boto3.resource("s3")
dynamodb = boto3.resource("dynamodb")
inventory_table = dynamodb.Table("Inventory")


def lambda_handler(event, context):
    """Process an inventory CSV file uploaded to Amazon S3."""

    print(
        "Event received by Lambda function: "
        + json.dumps(event, indent=2)
    )

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"]
    )

    local_filename = "/tmp/inventory.txt"

    try:
        s3.meta.client.download_file(
            bucket,
            key,
            local_filename
        )
    except Exception as error:
        print(error)
        print(
            f"Error getting object {key} from bucket {bucket}. "
            "Make sure the object exists and the bucket is in "
            "the same Region as this function."
        )
        raise

    with open(
        local_filename,
        mode="r",
        encoding="utf-8"
    ) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        row_count = 0

        for row in reader:
            row_count += 1

            print(
                row["store"],
                row["item"],
                row["count"]
            )

            try:
                inventory_table.put_item(
                    Item={
                        "Store": row["store"],
                        "Item": row["item"],
                        "Count": int(row["count"]),
                    }
                )
            except Exception as error:
                print(error)
                print("Unable to insert data into DynamoDB table")
                raise

    return f"{row_count} counts inserted"
