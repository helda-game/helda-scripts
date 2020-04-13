import http.client
import json
import os


def login():
    world_name = os.environ['HELDA_API_WORLD_NAME']
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
        headers = {
                    'Content-type': 'application/json',
                    'Authorization': 'Token ' + token
                    }
        url = "/worlds/find-world?world_name=" + world_name
        conn.request("GET", url, "", headers)
        response = conn.getresponse()
        if response.status == 200:
            global world_id
            world_id = json.loads(response.read().decode())["id"]
            return world_id
        else:
            dump_response("Error for url: " + url, response)
            return None
    else:
        dump_response("Authentication failed!", response)
        return None

def dump_response(title, response):
    print("=============================================")
    print(title)
    print(response.status)
    print(response.reason)
    print(response.read().decode())

# print(token)
if login():
    print(world_id)
else:
    print("Something went wrong!")
