from flask import Flask, request, Response
import json

app = Flask(__name__)

client = boto3.client()

@app.route("/", methods=['POST'])
def hello():
    client.put(json.loads(request.data))
    print('mensaje del cliente : {}'.format(client.get()))
    return Response(json.dumps(s3))

@app.route("/", methods=['GET'])
def hello_get():
    return client.get()

app.run(host = '0.0.0.0', port = 8080)
