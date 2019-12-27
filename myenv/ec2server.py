from flask import Flask, request, Response
import boto3
import json
import botocore
app = Flask(__name__)
s3 = boto3.client('s3')
@app.route("/<bucket>/<object>", methods=['POST'])
def hello(bucket, object):
    data = request.get_data()
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(bucket).download_file(object, str(data))
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
    
    print('mensaje del cliente : {}'.format(data))
    return format(data)

@app.route("/<bucket>/<algunpath>", methods=['GET'])
def hello_get(bucket, algunpath):
    return 'msj recibido'

app.run(host = '0.0.0.0', port = 8080)
