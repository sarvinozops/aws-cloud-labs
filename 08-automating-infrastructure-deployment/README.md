# Automating AWS Infrastructure Deployment

This project demonstrates how AWS infrastructure can be deployed and updated automatically by using Infrastructure as Code and a CI/CD workflow.

The solution uses AWS CloudFormation templates to deploy a static website, a reusable network layer, and a dynamic café application. AWS CodeCommit and CodePipeline were used to automatically update CloudFormation stacks after Git changes.

## Architecture

```mermaid
flowchart LR
    DEV[Developer] -->|git push| CC[AWS CodeCommit]
    CC --> CP[AWS CodePipeline]
    CP --> CF[AWS CloudFormation]

    CF --> NET[Network Stack]
    CF --> APP[Application Stack]

    NET --> VPC[VPC]
    VPC --> SUBNET[Public Subnet]
    VPC --> IGW[Internet Gateway]
    VPC --> RT[Route Table]

    APP --> SG[Security Group]
    APP --> EC2[EC2 Web Server]
    EC2 --> WEB[Apache + PHP + MariaDB Café App]

    CF --> S3[S3 Static Website]
Objectives
Create an Amazon S3 bucket by using CloudFormation.
Configure the S3 bucket for static website hosting.
Store CloudFormation templates in AWS CodeCommit.
Trigger automatic stack deployments with AWS CodePipeline.
Deploy a reusable VPC network layer.
Deploy a dynamic café application on Amazon EC2.
Recreate the infrastructure in a second AWS Region.
Use parameters, mappings, outputs, exports, and cross-stack references.
Technologies
AWS CloudFormation
AWS CodeCommit
AWS CodePipeline
Amazon S3
Amazon VPC
Amazon EC2
AWS Systems Manager Parameter Store
Git
YAML
Apache HTTP Server
PHP
MariaDB
Project Structure
08-automating-infrastructure-deployment/
├── README.md
├── templates/
│   ├── S3.yaml
│   ├── cafe-network.yaml
│   └── cafe-app.yaml
└── screenshots/
CloudFormation Templates
S3.yaml

Creates an S3 bucket and configures it for static website hosting.

Main features:

Static website hosting
index.html as the index document
Website URL as a CloudFormation output
Retain policy for the S3 bucket
cafe-network.yaml

Creates the network layer required by the application.

Resources include:

VPC
Internet Gateway
Internet Gateway attachment
Public subnet
Public route table
Internet route
Subnet route table association

The template exports the VPC ID and public subnet ID for use by the application stack.

cafe-app.yaml

Creates the dynamic café application layer.

Resources and configuration include:

EC2 security group
EC2 web server
Configurable instance type
Region-specific EC2 key pair mapping
Public subnet and VPC cross-stack imports
Apache, PHP, and MariaDB installation through EC2 User Data
Public IPv4 address as a stack output
CI/CD Deployment Flow
CloudFormation templates are edited in the development environment.
Changes are committed and pushed to AWS CodeCommit.
AWS CodePipeline detects the new commit.
CodePipeline passes the template to AWS CloudFormation.
CloudFormation creates or updates the required AWS resources.
Git Push
   ↓
AWS CodeCommit
   ↓
AWS CodePipeline
   ↓
AWS CloudFormation
   ↓
AWS Infrastructure
Multi-Region Deployment

The same CloudFormation templates were used to deploy the café infrastructure in two AWS Regions:

Environment	Region	Instance type	Key pair
Primary	us-east-1	t2.small	vockey
Secondary	us-west-2	t3.micro	cafe-oregon

The RegionMap mapping automatically selects the appropriate key pair for each supported Region.

Results
Static café website deployed successfully with Amazon S3.
Network stack deployed automatically through CodePipeline.
Application stack deployed automatically through CodePipeline.
Dynamic café website successfully connected to its local database.
Menu and order functionality verified.
Network and application infrastructure duplicated in a second AWS Region.
Security Notes
No AWS access keys, passwords, or private keys are included.
.pem files must never be committed to GitHub.
AWS account IDs, instance IDs, and public IP addresses should be hidden in portfolio screenshots.
SSH access from 0.0.0.0/0 was used only in the temporary lab environment. A production deployment should restrict SSH access to trusted IP addresses or use AWS Systems Manager Session Manager.
The deployed URLs belonged to a temporary AWS lab environment and might no longer be available.
Key Takeaways

This project demonstrates how Infrastructure as Code and CI/CD reduce manual configuration, improve repeatability, and make it easier to create matching environments across multiple AWS Regions.
