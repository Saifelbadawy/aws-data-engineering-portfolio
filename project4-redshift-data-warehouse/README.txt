# Project 4 — Amazon Redshift Data Warehouse

## Overview
This project implements a cloud data warehouse using Amazon Redshift Serverless. Sales data stored in Amazon S3 is loaded into Redshift using the COPY command and analyzed with SQL.

## Architecture
S3 → Redshift Serverless → Query Editor v2

## Technologies Used
- Amazon S3
- Amazon Redshift Serverless
- Query Editor v2
- SQL

## Key Steps
- Created a warehouse table in Redshift
- Loaded sales data from S3 using COPY
- Ran analytical SQL queries for revenue and profit reporting