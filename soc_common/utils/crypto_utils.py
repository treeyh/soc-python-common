# -*- encoding: utf-8 -*-

'''
@file           :crypto_utils.py
@description    :
@time           :2024-11-01 15:16:33
@author         :Tree
@version        :1.0
'''

import secrets

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

import os

def get_aes256_key():
  """生成一个 32 字节（256 位）的 AES-256 密钥

  Returns:
      _type_: _description_
  """  
  aes_key = secrets.token_bytes(32)
  return aes_key.hex()


def derive_aes_key(base_key: bytes, context_param: bytes) -> bytes:
  """使用 PBKDF2HMAC 基于已有的 AES-256 密钥派生新的 AES-256 密钥

  Args:
      base_key (bytes): _description_
      context_param (bytes): _description_

  Returns:
      bytes: _description_
  """    
  salt = os.urandom(16)  # 使用随机盐值提高安全性
  kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,  # 输出长度为 32 字节（256 位）
      salt=salt,
      iterations=100000,
      backend=default_backend()
  )
  derived_key = kdf.derive(base_key + context_param)
  return derived_key.hex()