import http.client
import json
import os


def login():
    protocol = os.environ['HELDA_API_PROTOCOL']
    host = os.environ['HELDA_API_HOST']
    email = os.environ['HELDA_API_EMAIL']
    password = os.environ['HELDA_API_PASSWORD']

    if protocol == 'http':
        conn = http.client.HTTPConnection(host)
    else:
        conn = http.client.HTTPSConnection(host)

    headers = {'Content-type': 'application/json'}
    login_details = {'email': email, 'password': password}
    conn.request("POST", "/auth/auth-bot", json.dumps(login_details), headers)
    response = conn.getresponse()
    if response.status == 200:
        global token
        token = json.loads(response.read().decode())["token"]

login()
print(token)
