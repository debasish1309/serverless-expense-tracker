💸 Serverless Expense Tracker

A fully serverless, cloud-native expense management system built with AWS Lambda, Amazon API Gateway, Amazon DynamoDB, and Python (Boto3). This solution eliminates infrastructure overhead while providing secure, scalable, and cost-effective expense tracking via RESTful APIs.

🚀 Features

Serverless backend powered by AWS Lambda

CRUD operations for managing expenses

RESTful API endpoints via Amazon API Gateway

NoSQL data storage with Amazon DynamoDB (On-Demand)

Written in Python using Boto3 for seamless AWS integration

Logging and observability using Amazon CloudWatch

API testing using Postman

⚙️ AWS Setup Guide

1. Create DynamoDB Table

Table Name: Expenses

Primary Key: expense_id (String)

Capacity Mode: On-Demand

2. Create & Configure Lambda Function

Runtime: Python 3.12

IAM Role: Grant DynamoDB Full Access

Function Name: ExpenseHandler

3. Lambda Logic

POST /expense → Add new expense

GET /expense?expense_id=xyz → Retrieve expense

PUT /expense → Update expense details

DELETE /expense?expense_id=xyz → Delete expense

See Python implementation: lambda/lambda_function.py

4. API Gateway Configuration

Create HTTP API

Map routes to Lambda functions as per HTTP method

Deploy and note the Invoke URL

5. Test with Postman or cURL

curl -X POST https://your-api-id.execute-api.region.amazonaws.com/expense \
-H "Content-Type: application/json" \
-d '{"amount": 50, "category": "Food", "date": "2025-03-05"}'

6. Monitoring & Optimization

Enable CloudWatch Logs

Tune Lambda memory and timeout settings

Use DynamoDB indexes if needed

7. Learnings & Outcomes

Gained hands-on experience with AWS serverless architecture

Deepened understanding of secure API design using API Gateway

Practiced data modeling and integration with Python & Boto3

Strengthened observability practices using Amazon CloudWatch

8. Future Enhancements

Integrate authentication using Amazon Cognito

Add a frontend using React/Next.js

Visualize expenses with Amazon QuickSight or Power BI

Feel free to fork, star, or contribute!Built using AWS by Debasish

