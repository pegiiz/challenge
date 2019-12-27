import requests, json

response = requests.get("http://0.0.0.0:8080/challengemeli/asdf.txt")
r = requests.post("http://0.0.0.0:8080/challengemeli/asdf.txt",'nombre' )
print(response.content)
