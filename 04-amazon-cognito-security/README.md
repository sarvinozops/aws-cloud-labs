# Securing Applications with Amazon Cognito

## Lab Overview

This AWS guided lab demonstrates how to secure the Birds web application by using Amazon Cognito for authentication and authorization.

The application uses an Amazon Cognito User Pool to authenticate users and an Amazon Cognito Identity Pool to provide temporary AWS credentials for accessing Amazon DynamoDB.

## Objectives

- Create an Amazon Cognito User Pool
- Create standard and administrator users
- Configure an Administrators group
- Integrate the application with the User Pool
- Configure an Amazon Cognito Identity Pool
- Generate temporary AWS credentials
- Access Amazon DynamoDB securely
- Test authentication and role-based access

## AWS Services Used

- Amazon Cognito
- Amazon S3
- Amazon CloudFront
- Amazon DynamoDB
- AWS Cloud9
- Node.js

## Authentication Flow

```text
User
  |
  v
CloudFront
  |
  v
Birds Web Application
  |
  v
Cognito User Pool
  |
  v
Authentication Token
Authorization Flow
User Pool Token
  |
  v
Cognito Identity Pool
  |
  v
Temporary AWS Credentials
  |
  v
Amazon DynamoDB
Lab Implementation
1. Prepared the environment

The Birds application was installed in AWS Cloud9. The setup process created the S3 bucket, CloudFront distribution, Node.js server, and supporting AWS resources.

2. Reviewed the Birds application

The application was successfully accessed through Amazon CloudFront.

Before Cognito configuration, protected pages could not use an authentication provider.

3. Created the Cognito User Pool

A User Pool named bird_app was created.

The bird_app_client application client was configured to support username and password authentication.

A Cognito managed-login domain was configured.

4. Created users and groups

Two users were created:

testuser — standard user
admin — administrator

An Administrators group was created, and the admin user was added to it.

5. Tested User Pool authentication

The testuser account successfully logged in and accessed the protected Sightings page.

The admin account successfully accessed the protected Site Administration page.

6. Configured the Identity Pool

The existing Identity Pool was connected to the Cognito User Pool and application client.

7. Validated temporary AWS credentials

The application successfully received temporary AWS credentials and connected to the BirdSightings DynamoDB table.

Final Result

All lab tasks were completed successfully.

Final score: 30/30

Security Benefits
User passwords are centrally managed by Amazon Cognito.
Protected pages require successful authentication.
Administrator access is controlled through a Cognito group.
No permanent AWS credentials are stored in the application.
Temporary credentials are used for DynamoDB access.
Skills Demonstrated
Amazon Cognito User Pool configuration
Amazon Cognito Identity Pool configuration
User authentication
Role-based access control
Temporary AWS credentials
DynamoDB authorization
CloudFront and S3 web application delivery
