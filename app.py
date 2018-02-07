from flask import Flask
from flask import render_template
import code
import boto3
app = Flask(__name__)

sts = boto3.client(
    'sts',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
    )

@app.route("/")
def hello():
    cred = sts.get_federation_token(
    Name='your_authenticated_user',
    Policy='{"Version": "2012-10-17","Statement": [{"Sid": "VisualEditor0","Effect": "Allow","Action": "s3:*","Resource": ["arn:aws:s3:::<your-bucket-name-here>","arn:aws:s3:::<your-bucket-name-here>/*"]}]}',
    DurationSeconds=900
    )
    access_key_id = cred['Credentials']['AccessKeyId']
    session_token = cred['Credentials']['SessionToken']
    secret_access_key = cred['Credentials']['SecretAccessKey']
    return render_template('test.html', cred=cred)