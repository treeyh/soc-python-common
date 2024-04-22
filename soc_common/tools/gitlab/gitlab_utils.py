# -*- encoding: utf-8 -*-

'''
@file           :gitlab_utils.py
@description    :
@time           :2024-03-15 18:07:51
@author         :Tree
@version        :1.0
'''

import requests

_gitlab_pre_api = 'https://gitlab.snowballtech.com/api/v4'
_gitlab_session = 'f9a14bf8512cd02ddefa42b3dbe81c84'

# def get_auth_token():

#   url = 'https://gitlab.snowballtech.com/oauth/authorize?client_id=APP_ID&redirect_uri=REDIRECT_URI&response_type=code&state=STATE&scope=REQUESTED_SCOPES&code_challenge=CODE_CHALLENGE&code_challenge_method=S256'

#   print(url)

def get_all_projects():
  url = '%s/projects' % (_gitlab_pre_api)
  
  headers = {
    'Cookie': '_gitlab_session='+_gitlab_session
  }

  resp = requests.get(url = url, headers=headers)
  
  projects = resp.json()

  print(len(projects))


def get_project_access():
  url = '%s/projects/%d/access_requests' % (_gitlab_pre_api, 825)
  
  headers = {
    'Cookie': '_gitlab_session='+_gitlab_session
  }

  resp = requests.get(url = url, headers=headers)
  
  r = resp.json()

  print(r)

  