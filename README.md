# 💸 Serverless Expense Tracker

A fully serverless, cloud-native expense management system built with **AWS Lambda**, **Amazon API Gateway**, **Amazon DynamoDB**, and **Python (Boto3)**. This solution eliminates infrastructure overhead while providing secure, scalable, and cost-effective tracking of personal expenses via RESTful APIs.

## 🚀 Features

- Serverless backend powered by AWS Lambda
- CRUD operations for managing expenses
- RESTful API endpoints via API Gateway
- NoSQL data storage with Amazon DynamoDB (On-Demand)
- Written in Python using Boto3 for seamless AWS integration
- Logging and observability with Amazon CloudWatch
- API testing with Postman

## 🧱 Architecture

Client ↔️ API Gateway ↔️ Lambda (Python) ↔️ DynamoDB

## 📁 Project Structure

serverless-expense-tracker/ ├── lambda/ │   └── lambda_function.py ├── postman/ │   └── ExpenseTrackerCollection.json ├── requirements.txt ├── architecture.png └── README.md

## ⚙️ AWS Setup Guide

### 1. Create DynamoDB Table

- Table Name: `Expenses`
- Primary Key: `expense_id` (String)
- Capacity Mode: On-Demand

### 2. Create & Configure Lambda Function

- Runtime: Python 3.x
- IAM Role: Grant DynamoDB Full Access
- Function Name: `ExpenseHandler`

### 3. Lambda Logic

- `POST /expense` → Add new expense  
- `GET /expense?expense_id=xyz` → Retrieve expense  
- `PUT /expense` → Update expense details  
- `DELETE /expense?expense_id=xyz` → Delete expense  

> For Python implementation, see [`lambda/lambda_function.py`](lambda/lambda_function.py)

### 4. API Gateway Configuration

- Create HTTP API
- Map routes to Lambda functions as per HTTP method
- Deploy and note the Invoke URL

### 5. Test with Postman or cURL

```bash
curl -X POST https://your-api-id.execute-api.region.amazonaws.com/expense \
-H "Content-Type: application/json" \
-d '{"amount": 50, "category": "Food", "date": "2025-03-05"}'
