import os
import binascii
from Crypto.PublicKey import ECC
from Crypto.Cipher import ECIES

def generate_key_pair():
    """
    生成公私钥对

    :return: 公钥、私钥
    """
    params = ECC.generate_parameters(curve='secp256k1')
    key_pair = ECC.generate_key_pair(params)
    return key_pair.public_key(), key_pair.private_key()

def encrypt(data, public_key):
    """
    使用公钥加密数据

    :param data: 要加密的数据
    :param public_key: 公钥
    :return: 加密后的数据
    """
    cipher = ECIES.new(public_key, ECIES.Mode.CBC, None)
    ciphertext = cipher.encrypt(data)
    return binascii.b2a_base64(ciphertext).decode()

def decrypt(ciphertext, private_key):
  """
  使用私钥解密数据

  :param ciphertext: 要解密的数据
  :param private_key: 私钥
  :return: 解密后的数据
  """
  cipher = ECIES.new(private_key, ECIES.Mode.CBC, None)
  plaintext = cipher.decrypt(binascii.a2b_base64(ciphertext))
  return plaintext

def run():
  # 生成公私钥对
  public_key, private_key = generate_key_pair()

  # 加密数据
  data = "Hello, world!"
  ciphertext = encrypt(data, public_key)

  # 解密数据
  plaintext = decrypt(ciphertext, private_key)

  # 输出结果
  print("加密后的数据：", ciphertext)
  print("解密后的数据：", plaintext)