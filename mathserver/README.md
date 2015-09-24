AWS Math Service
================

A simple web service demonstrating several features of AWS development
and deployment.

- web service that does simple arithmetic
- request logging via SQS
- site pages in git, deployed via S3
- command line service startup, no logging in to box


Service Description
-------------------

App Server

- runs http service
- performs basic arithmetic
- logs activity to queue
- v2: put behind load balancer, add multiple boxes
- http://apps.mhmath.net/cgi-bin/mathserver?op=add&x=4&y=5

Admin Box

- collects and prints usage stats via SQS

Testing

- generate traffic, sends to load balanced service

DevOp Requirements

- all boxes started automatically
- when boxes start up, service starts
- can deploy new code to running boxes

Deployment

- all code in git
- git syncs to S3 bucket
- nodes updated from S3 bucket
- services controlled by command line on laptop
- service monitoring on laptop

Service Configuration

- V1 is a simple service, with a single box server.
- V2 puts the service behind a load balancer.  multiple app servers

Profile Information

- AZ: usa-west-2 (oregeon)
- AMI: img-master (based on: amazon linux, t2.micro)
- IAM role: general (s3, sqs)
- Instances: www1, www2, adm
- bucket: mhmathadm-www
- queue: mhmath


V1 Configuration
----------------

Architecture:

- one mgmt box
- one web service box
- both boxes, same setup

Load Balanced DNS:		apps.mhmath.net

Setup Notes
===========

role descriptions

- admin:  AdministratorAccess, AmazonSQSFullAccess
- general: AmazonSQSFullAccess, AmazonS3FullAccess

User Data Config

```
#!/bin/bash
# this will set up an instance to be httpd-ready
yum update -y
yum install -y httpd
service httpd start
chkconfig httpd on
groupadd www
usermod -a -G www ec2-user
chown -R root:www /var/www
chmod 2775 /var/www
aws --region=us-west-2 s3 cp s3://mhmathadm.www /var/www --recursive
find /var/www -type d -exec chmod 2775 {} +
find /var/www/cgi-bin -type f -exec chmod 2775 {} +
find /var/www/utils -type f -exec chmod 2775 {} +
```

Network Configuration (v2)
==========================

- apps.mhmath.net points to the load balancer
- the load balancer sits in front of 2 or more nodes
- the stats collector sits on an admin box
- (set cname on DNS server to point to load balancer)

Load Balancer Configuration
---------------------------

aws --profile=mhmathadm elb create-load-balancer --load-balancer-name=mathlb --listeners=Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80 --availability-zone=us-west-2a

Document Management
-------------------

- edit files in git
- run command:  s3tool sync
- this copies modified files onto an s3 bucket
- system nodes refresh themselves from this bucket automatically
- on sync, nodes send a logging messages


Tests
-----

- test1, test1a: simplest tests for regression purposes
- test2: more combinations, load
