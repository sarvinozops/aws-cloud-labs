# Building Decoupled Applications with Amazon SQS and SNS

## Overview

This project demonstrates how to transform a tightly coupled image-processing application into a decoupled and more reliable architecture by using Amazon SQS and Amazon SNS.

The application accepts PNG images, stores them in Amazon S3, processes them into resized and tinted images, and tracks processing information in Amazon DynamoDB.

The lab was completed in two phases:

- **Phase 1:** Tightly coupled architecture
- **Phase 2:** Decoupled architecture using Amazon SQS and Amazon SNS

## Objectives

- Review how an image-processing web application works
- Configure Amazon S3 bucket permissions
- Configure S3 event notifications
- Create an Amazon SNS topic
- Create an Amazon SQS queue
- Subscribe Amazon SQS to an SNS topic
- Configure an SNS email subscription
- Implement SQS polling
- Compare tightly coupled and decoupled architectures

## AWS Services Used

- Amazon EC2
- Amazon S3
- Amazon DynamoDB
- Amazon Simple Queue Service — SQS
- Amazon Simple Notification Service — SNS
- AWS IAM
- Node.js

---

## Phase 1: Tightly Coupled Architecture

In Phase 1, the web server communicates directly with the application server.

```mermaid
flowchart LR
    User[User] --> Web[Web Server]
    Web --> S3[Amazon S3]
    Web --> DDB[Amazon DynamoDB]
    Web --> App[Application Server]
    App --> S3
    App --> DDB
    S3 --> UserWorkflow
The user uploads an image through the web application.
The web server stores the original image in Amazon S3.
Image metadata and processing status are stored in DynamoDB.
The web server directly calls the application server.
The application server resizes and tints the image.
The processed image is uploaded back to Amazon S3.
The browser displays the completed image.
Lab IDE

Phase 1 S3 Permissions

Phase 1 Bucket Policy

Image Tinter Application

Processed Image

Phase 1 Analysis

The web server and application server are tightly coupled. The web server must wait for the application server to complete image processing.

If the application server becomes unavailable, the whole image-processing workflow can fail.

Phase 2: Decoupled Architecture

In Phase 2, Amazon SNS and Amazon SQS are introduced between the storage and processing components.

Decoupled Workflow
The user uploads an image through the improved web application.
The web server stores the image in the Phase 2 S3 bucket.
Amazon S3 sends an event notification to Amazon SNS.
Amazon SNS sends the message to:
The Amazon SQS queue
The subscribed email address
The application server polls the SQS queue.
The application server receives the image information.
The original image is downloaded from S3.
The image is resized and tinted.
The processed image is saved back to S3.
DynamoDB processing status is updated.
The browser displays the completed image.
Amazon SQS Queue

A Standard SQS queue named ImageApp was created to store image-processing messages.

Messages remain in the queue until the application server is available to process them.

Amazon SNS Topic

An SNS topic named uploadnotification was created.

The SNS topic receives S3 event notifications and distributes them to multiple subscribers.

Phase 2 S3 Permissions

Public access blocking was disabled for the lab bucket, and access was restricted through a bucket policy.

Phase 2 Bucket Policy

S3 Event Notification

An event notification named SendtoSns was configured for all object creation events.

Amazon S3 → Amazon SNS

SNS to SQS Subscription

The ImageApp SQS queue was subscribed to the uploadnotification SNS topic.

Amazon SNS → Amazon SQS

SNS Email Subscription

An email endpoint was subscribed to the SNS topic and successfully confirmed.

Amazon SNS → Email

Testing the Improved Application

The improved application runs on a separate web-server port and includes controls for:

Looking up images
Uploading images
Polling the SQS queue
Stopping SQS polling

Before SQS Polling

After the image was uploaded, it was stored in Amazon S3 and a message was placed in the SQS queue.

The image remained unprocessed until polling started.

After SQS Polling

After selecting Poll SQS, the application server received and processed the queued message.

The image was resized, tinted, and saved back to Amazon S3.

Final Result

The decoupled architecture was successfully implemented and tested.

Browser
   ↓
Web Server
   ↓
Amazon S3
   ↓
Amazon SNS
   ├── Email Notification
   └── Amazon SQS
           ↓
    Application Server
           ↓
    Processed Image in S3

The final lab score was:

30/30

Key Takeaways
Tight coupling creates direct dependencies between application components.
Amazon SQS stores messages until consumers are ready to process them.
Amazon SNS can distribute one event to multiple subscribers.
S3 event notifications can automatically start asynchronous workflows.
Decoupled applications provide better reliability, scalability, and availability.
If the application server becomes unavailable, messages remain safely stored in SQS.
Polling allows the application server to process queued messages when it is ready.
Security Notes
AWS Account IDs were removed or hidden from public screenshots.
Public IP addresses were removed or hidden.
SQS queue URLs and resource ARNs were redacted where necessary.
No AWS credentials or private keys were committed to the repository.
Bucket access was restricted to a specific source IP during the lab.
Project Structure
09-decoupled-applications-sqs-sns/
├── README.md
└── screenshots/
    ├── 01-lab-ide-open.png
    ├── 02-phase1-bucket-permissions.png
    ├── 03-phase1-bucket-policy.png
    ├── 04-phase1-image-tinter-app.png
    ├── 05-phase1-processed-image.png
    ├── 06-sqs-imageapp-queue.png
    ├── 08-phase2-bucket-permissions.png
    ├── 09-phase2-bucket-policy.png
    ├── 10-s3-event-notification-created.png
    ├── 11-sqs-sns-subscription.png
    ├── 12-sns-email-subscription-confirmed.png
    ├── 13-phase2-image-tinter-improved.png
    ├── 14-phase2-image-uploaded-before-polling.png
    ├── 15-phase2-processed-images.png
    └── 16-final-score.png

