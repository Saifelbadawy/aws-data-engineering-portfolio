\#  Reusable S3 Data Lake using AWS CloudFormation



\##  Overview

This project demonstrates how to provision a reusable S3-based data lake foundation using AWS CloudFormation. The infrastructure is defined using a YAML template and deployed as a CloudFormation stack, creating separate storage layers for raw and processed data.



\---



\##  Architecture

CloudFormation → S3 (Raw Bucket + Processed Bucket)



\---



\##  Technologies Used

\- AWS CloudFormation  

\- Amazon S3  



\---



\##  Workflow

1\. Created a CloudFormation template using YAML  

2\. Defined parameters for dynamic bucket naming  

3\. Deployed the template as a CloudFormation stack  

4\. Automatically provisioned:

&#x20;  - Raw data bucket  

&#x20;  - Processed data bucket  

5\. Verified resources using CloudFormation Outputs  

6\. Uploaded sample files to both buckets  



\---



\## Resources Created



\### Raw Bucket

\- Stores original, unprocessed data  

\- Versioning enabled  

\- Lifecycle rule applied (auto-deletes objects after 30 days)  



\###  Processed Bucket

\- Stores cleaned and transformed data  

\- Versioning enabled  



\---



\## Key Features

\- Infrastructure as Code (IaC)  

\- Parameterized resource creation  

\- Automated deployment using CloudFormation  

\- Data lake design (raw vs processed separation)  

\- Versioning for data protection  

\- Lifecycle rule for cost optimization  



\---



&#x20;Outputs

The CloudFormation stack provides:

\- Raw bucket name  

\- Processed bucket name  



These outputs make it easier to reuse resources in future projects.



\---





\##  What I Learned

\- How to define AWS infrastructure using YAML  

\- Understanding CloudFormation stacks and templates  

\- Using Parameters, Resources, and Outputs  

\- Automating AWS resource provisioning  

\- Designing a simple data lake architecture  



\---





