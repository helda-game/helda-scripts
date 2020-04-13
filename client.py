import http.client
import json
import os


email = os.environ['HELDA_API_EMAIL']
password = os.environ['HELDA_API_PASSWORD']

print(email)
print(password)

conn = http.client.HTTPConnection('localhost:3000')

headers = {'Content-type': 'application/json'}

# foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
# json_data = json.dumps(foo)


conn.request("GET", "/meta/env-info")
response = conn.getresponse()
print(response.status, response.reason)
print(response.read().decode())
