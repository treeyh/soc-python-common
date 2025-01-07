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

def get_aes512_key():
    """生成一个 32 字节（256 位）的 AES-256 密钥

    Returns:
        _type_: _description_
    """  
    aes_key = secrets.token_bytes(64)
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


def derive_aes512_key(base_key: bytes, context_param: bytes) -> bytes:
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
        length=64,  # 输出长度为 32 字节（256 位）
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    derived_key = kdf.derive(base_key + context_param)
    return derived_key.hex()

def encode_aes_cbc():
    # 示例数据
    data = "Hello, World! This is AES-128 CBC encryption."

    # 密钥必须是 16 字节 (128 位)
    key = b'Sixteen byte key'  # 16 字节密钥

    # 生成一个随机的 16 字节 IV
    iv = get_random_bytes(AES.block_size)

    # 使用 AES-128 CBC 模式加密
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 加密数据（需要填充到 16 字节的倍数）
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
    print(f"Ciphertext (hex): {binascii.hexlify(ciphertext)}")

    # 使用相同的 IV 和密钥进行解密
    decipher = AES.new(key, AES.MODE_CBC, iv)

    # 解密并去除填充
    plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size).decode()
    print(f"Plaintext: {plaintext}")