# file -- pkg.common.py --

import requests
import json
import yaml

requests.packages.urllib3.disable_warnings()

def post_json(url: str, payload):
    headers = { 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8' }
    response = requests.post(url, data=payload, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def get_json(url: str, params):
    headers = { 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8' }
    response = requests.get(url, params=params, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def put_json(url: str, payload):
    headers = { 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8' }
    response = requests.put(url, data=payload, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def patch_json(url: str, payload):
    headers = { 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8' }
    response = requests.patch(url, data=payload, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def delete(url: str, payload):
    headers = { 'Content-Type': 'application/json; charset=utf-8' }
    response = requests.delete(url, data=payload, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def read_json_file(file="example.json"):
    with open(file, 'r') as data:
        return json.load(data)

def read_yaml_file(file="example.yaml"):
    with open(file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
