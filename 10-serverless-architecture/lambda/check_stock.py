# Check-Stock Lambda function
#
# Triggered by DynamoDB Streams when inventory records are inserted.
# If an item's count is zero, an alert is published to Amazon SNS.

import json

import boto3


sns = boto3.client("sns")


def lambda_handler(event, context):
    """Check inventory records and notify when Count equals zero."""

    print(
        "Event received by Lambda function: "
        + json.dumps(event, indent=2)
    )

    topic_arn = next(
        (
            topic["TopicArn"]
            for topic in sns.list_topics()["Topics"]
            if topic["TopicArn"].endswith(":NoStock")
        ),
        None,
    )

    if topic_arn is None:
        raise RuntimeError("NoStock SNS topic was not found")

    alerts_sent = 0

    for record in event.get("Records", []):
        new_image = record.get("dynamodb", {}).get("NewImage")

        if not new_image:
            continue

        count = int(new_image["Count"]["N"])

        if count == 0:
            store = new_image["Store"]["S"]
            item = new_image["Item"]["S"]

            message = f"{store} is out of stock of {item}"

            print(message)

            sns.publish(
                TopicArn=topic_arn,
                Message=message,
                Subject="Inventory Alert!",
            )

            alerts_sent += 1

    return {
        "records_processed": len(event.get("Records", [])),
        "alerts_sent": alerts_sent,
    }
