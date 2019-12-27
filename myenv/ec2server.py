from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/<algunpath>", methods=['POST'])
def hello(algunpath):
    data = request.get_data()
    print('mensaje del cliente : {}'.format(data))
    return Response(algunpath)

@app.route("/", methods=['GET'])
def hello_get():
    return "asd"

app.run(host = '0.0.0.0', port = 8080)
