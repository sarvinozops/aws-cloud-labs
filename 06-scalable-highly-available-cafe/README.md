# Scalable and Highly Available Café Web Application

## Project Overview

This challenge lab demonstrates how to build a scalable and highly available web application architecture on AWS.

The Café web application was originally running on a single EC2 instance. To prepare the application for a large increase in traffic, the architecture was redesigned to distribute requests across multiple EC2 instances in two Availability Zones.

## Objectives

- Inspect the existing VPC architecture
- Configure networking across two Availability Zones
- Create a NAT Gateway for the second private subnet
- Create an EC2 Launch Template
- Create an Auto Scaling Group
- Configure automatic scaling based on CPU utilization
- Create an Application Load Balancer
- Connect the Auto Scaling Group to a Target Group
- Test load balancing
- Test automatic scale-out under CPU load

## AWS Services Used

- Amazon VPC
- Amazon EC2
- Amazon EC2 Auto Scaling
- Elastic Load Balancing
- Application Load Balancer
- NAT Gateway
- Amazon Machine Images
- AWS Systems Manager Session Manager
- Amazon CloudWatch

## Architecture

The final architecture includes:

- An internet-facing Application Load Balancer in two public subnets
- EC2 web servers in two private subnets
- An Auto Scaling Group distributed across two Availability Zones
- NAT Gateways for outbound internet access from private instances
- A Target Group that routes HTTP traffic to healthy EC2 instances

```text
Internet Users
      |
Application Load Balancer
      |
--------------------------------
|                              |
Private Subnet 1         Private Subnet 2
EC2 Web Servers          EC2 Web Servers
|                              |
NAT Gateway 1            NAT Gateway 2
Implementation
1. Existing Environment Inspection

The existing VPC, subnets, route tables, security group, EC2 instance and AMI were inspected before modifying the architecture.

2. Private Subnet Internet Connectivity

Private Subnet 1 already used a NAT Gateway for outbound internet connectivity.

A second NAT Gateway was created in Public Subnet 2.

Private Route Table 2 was updated with a default route to the new NAT Gateway.

3. EC2 Launch Template

A Launch Template was created with the following configuration:

AMI: Cafe WebServer Image
Instance type: t2.micro
Security group: CafeSG
IAM instance profile: CafeRole
Instance tag: Name = webserver

4. Auto Scaling Group

An Auto Scaling Group was created across Private Subnet 1 and Private Subnet 2.

Configuration:

Desired capacity: 2
Minimum capacity: 2
Maximum capacity: 6
Scaling metric: Average CPU utilization
Target CPU utilization: 25%
Instance warmup: 60 seconds

Two EC2 instances were initially launched across two Availability Zones.

5. Application Load Balancer

An internet-facing Application Load Balancer was created in the two public subnets.

The load balancer listens for HTTP traffic on port 80 and forwards requests to the Café Target Group.

Both EC2 web servers passed the Target Group health checks.

6. Application Test

The Café application was accessed through the Application Load Balancer DNS name using the /cafe path.

7. Automatic Scaling Test

A CPU stress test was started on one of the EC2 web servers:

sudo amazon-linux-extras install epel -y
sudo yum install stress -y
stress --cpu 1 --timeout 600

When CPU utilization exceeded the configured target, the Auto Scaling Group automatically launched additional EC2 instances.

The number of web servers increased from 2 to 6.

## Results

The final environment successfully:

- Distributed traffic across healthy EC2 instances
- Operated across two Availability Zones
- Automatically scaled from 2 to 6 instances
- Maintained application availability during increased CPU load
- Kept application servers inside private subnets
- Allowed users to access the application through a public load balancer

## Security Notes

Sensitive information such as AWS account IDs, resource IDs, public IP addresses, ARNs and private key files was excluded or hidden from the repository.

The downloaded `.pem` private key was not committed to GitHub.
