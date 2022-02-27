import requests
import os

token = os.getenv('token_ya')


def create_folder(access_token_ya):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': access_token_ya,
               'Content-Type': 'application/json'}
    params = {'path': 'new_folder'}
    response = requests.put(url=url, headers=headers, params=params)
    return response.status_code
