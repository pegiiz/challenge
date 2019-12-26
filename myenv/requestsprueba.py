import requests, json

response = requests.get("http://0.0.0.0:8080/")
r = requests.post("http://0.0.0.0:8080/", json={'message': 'hola'})
print(response.content)
