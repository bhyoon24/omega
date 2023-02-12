import requests
import platform

import config as config
import auth as auth
# 아래 값은 필요시 수정
protocol = 'https'
domain = 'api.solapi.com'
prefix = ''

default_agent = {
    'sdkVersion': 'python/4.2.0',
    'osPlatform': platform.platform() + " | " + platform.python_version()
}

def get_url(path):
  url = '%s://%s' % (protocol, domain)
  if prefix != '':
    url = url + prefix
  url = url + path
  return url

def send_many(data):
    data['agent'] = default_agent
    return requests.post(get_url('/messages/v4/send-many'),
                         headers=auth.get_headers(config.api_key, config.api_secret), json=data)


def send_one(data):
    data['agent'] = default_agent
    return requests.post(get_url('/messages/v4/send'),
                         headers=auth.get_headers(config.api_key, config.api_secret),
                         json=data)


def post(path, data):
    return requests.post(config.get_url(path), headers=auth.get_headers(config.api_key, config.api_secret), json=data)


def put(path, data, headers=None):
    if headers is None:
        headers = {}
    headers.update(auth.get_headers(config.api_key, config.api_secret))
    return requests.put(config.get_url(path), headers=headers, json=data)


def get(path, headers=None):
    if headers is None:
        headers = {}
    headers.update(auth.get_headers(config.api_key, config.api_secret))
    return requests.get(config.get_url(path), headers=headers)


def delete(path, data):
    if data is None:
        return requests.delete(config.get_url(path), headers=auth.get_headers(config.api_key, config.api_secret))
    else:
        return requests.delete(config.get_url(path), headers=auth.get_headers(config.api_key, config.api_secret),
                               json=data)
