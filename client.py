import http.client
import json
import os

protocol = os.environ['HELDA_API_PROTOCOL']
host = os.environ['HELDA_API_HOST']

# global api_headers
# global world_id

def dump_response(url, response, response_body):
    print("=============================================")
    print(url + " response: ")
    print(response.status)
    print(response.reason)
    print(response_body)

def get(url, on_success, on_error=dump_response):
    call_service("GET", url, None, on_success, on_error)

def post(url, body, on_success, on_error=dump_response):
    call_service("POST", url, body, on_success, on_error)

def call_service(http_method, url, body, on_success, on_error=dump_response):
    if protocol == 'http':
        conn = http.client.HTTPConnection(host)
    else:
        conn = http.client.HTTPSConnection(host)
    conn.request(http_method, url, json.dumps(body) if body else None, api_headers)
    response = conn.getresponse()
    if response.status == 200:
        on_success(json.loads(response.read().decode()))
    else:
        on_error(url, response, response.read().decode())

def login():
    email = os.environ['HELDA_API_EMAIL']
    password = os.environ['HELDA_API_PASSWORD']

    global api_headers
    api_headers = {'Content-type': 'application/json'}

    post("/auth/auth-bot", {'email': email, 'password': password}, on_login)

def on_login(response_body):
    global api_headers
    api_headers = {
                    'Content-type': 'application/json',
                    'Authorization': 'Token ' + response_body["token"]
                    }
    print("Token: " + response_body["token"])
    world_name = os.environ['HELDA_API_WORLD_NAME']
    get("/worlds/find-world?world_name=" + world_name, on_world_loaded)

def on_world_loaded(response_body):
    global world_id
    world_id = response_body["id"]
    print("world_id: " + world_id)

def publish_update(iteration_ctx):
    iteration_ctx['world_id'] = world_id
    post(
        "/world-updates/publish-world-update",
        iteration_ctx,
        lambda r: print("World updated! ")
        )
# login()
# if world_id:
#     print("Success!")
    #Postprocessing goes here!
