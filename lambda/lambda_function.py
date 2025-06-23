import json
import boto3
import uuid
import logging

# Setup
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Expenses')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    method = event.get('httpMethod')
    logger.info(f"Received {method} request: {event}")

    if method == 'POST':
        return add_expense(event)
    elif method == 'GET':
        return get_expense(event)
    elif method == 'PUT':
        return update_expense(event)
    elif method == 'DELETE':
        return delete_expense(event)
    else:
        return response(405, {'error': 'Method Not Allowed'})

def add_expense(event):
    try:
        data = json.loads(event['body'])
        expense_id = str(uuid.uuid4())
        table.put_item(Item={"expense_id": expense_id, **data})
        return response(201, {"message": "Expense added", "id": expense_id})
    except Exception as e:
        logger.error(f"Add Error: {str(e)}")
        return response(500, {"error": "Failed to add expense"})

def get_expense(event):
    try:
        expense_id = event['queryStringParameters']['expense_id']
        result = table.get_item(Key={"expense_id": expense_id})
        item = result.get('Item')
        if item:
            return response(200, item)
        else:
            return response(404, {"message": "Expense not found"})
    except Exception as e:
        logger.error(f"Get Error: {str(e)}")
        return response(500, {"error": "Failed to retrieve expense"})

def update_expense(event):
    try:
        data = json.loads(event['body'])
        expense_id = data['expense_id']
        table.update_item(
            Key={"expense_id": expense_id},
            UpdateExpression="SET amount = :a, category = :c, date = :d",
            ExpressionAttributeValues={
                ":a": data['amount'],
                ":c": data['category'],
                ":d": data['date']
            }
        )
        return response(200, {"message": "Expense updated"})
    except Exception as e:
        logger.error(f"Update Error: {str(e)}")
        return response(500, {"error": "Failed to update expense"})

def delete_expense(event):
    try:
        expense_id = event['queryStringParameters']['expense_id']
        table.delete_item(Key={"expense_id": expense_id})
        return response(200, {"message": "Expense deleted"})
    except Exception as e:
        logger.error(f"Delete Error: {str(e)}")
        return response(500, {"error": "Failed to delete expense"})

def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }