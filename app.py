from flask import Flask, render_template, request
import boto3
from datetime import datetime

app = Flask(__name__)

# DynamoDB connection
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('registration-table')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')

    table.put_item(
        Item={
            'email': email,
            'name': name,
            'created_at': datetime.utcnow().isoformat()
        }
    )

    return "Registration successful"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
