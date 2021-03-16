import requests
from decouple import config

api_key = config("api_key")
url = "https://api.sendgrid.com/?key={}"


def send_post():
    resp = requests.post(url + api_key)
    print(resp.json)


def get_post():
    resp = requests.get(url)
    print(resp.json)