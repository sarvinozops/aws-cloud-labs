# Automating Infrastructure Deployment with AWS CloudFormation

## Project Overview

This project demonstrates how to automate AWS infrastructure deployment using AWS CloudFormation and reusable YAML templates.

The infrastructure was separated into two layers:

- Networking layer
- Application layer

The application stack imported the VPC and subnet values exported by the networking stack.

## Objectives

- Deploy a VPC networking layer
- Deploy an EC2 application layer
- Use cross-stack references
- Update an existing CloudFormation stack
- Explore templates with Infrastructure Composer
- Delete a stack while retaining an EBS snapshot

## Architecture

```text
lab-network stack
├── VPC
├── Public Subnet
├── Internet Gateway
├── Route Table
└── Public Route

lab-application stack
├── EC2 Instance
├── Security Group
├── EBS Volume
└── Web Application
Repository Structure
07-cloudformation-infrastructure/
├── README.md
├── templates/
│   ├── lab-network.yaml
│   ├── lab-application.yaml
│   └── lab-application2.yaml
└── screenshots/
    ├── 01-network-stack-complete.png
    ├── 02-network-stack-resources.png
    ├── 03-network-stack-outputs.png
    ├── 04-application-stack-complete.png
    ├── 05-application-stack-outputs.png
    ├── 06-web-application-running.png
    ├── 07-security-group-http-rule.png
    ├── 08-application-stack-update-complete.png
    ├── 09-security-group-https-rule.png
    ├── 10-infrastructure-composer-application.png
    ├── 11-infrastructure-composer-network.png
    └── 12-ebs-snapshot-created.png
Task 1: Networking Layer

The lab-network.yaml template created the VPC networking layer.

Resources included:

VPC
Public subnet
Internet Gateway
Public route table
Public route
Route table association

The stack exported the VPC ID and public subnet ID for use by another stack.

Task 2: Application Layer

The lab-application.yaml template created:

EC2 instance
Web server security group
EBS volume
Sample web application

The application stack used Fn::ImportValue to import the VPC and subnet IDs from the lab-network stack.

The sample application was successfully accessed through the EC2 public DNS address.

Task 3: Stack Update

Initially, the security group allowed HTTP traffic on port 80.

The stack was updated using lab-application2.yaml.

The updated template added HTTPS traffic on port 443 without recreating the complete infrastructure.

Opening port 443 does not automatically configure HTTPS. A certificate and web server TLS configuration would also be required.

Task 4: Infrastructure Composer

AWS Infrastructure Composer was used to inspect the relationships between resources visually.

Task 5: Stack Deletion and Snapshot

The application stack was deleted after testing.

The EBS volume resource used:

DeletionPolicy: Snapshot

CloudFormation therefore created an EBS snapshot before deleting the volume.

The networking stack remained available because it was managed separately.

Key Concepts
Infrastructure as Code
AWS CloudFormation
YAML templates
Stack parameters and outputs
Cross-stack references
Fn::ImportValue
Stack updates
Infrastructure Composer
Deletion policies
EBS snapshots
Conclusion

This project demonstrated how AWS infrastructure can be deployed, updated, visualized, and deleted through a repeatable Infrastructure as Code process.
