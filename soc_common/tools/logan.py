#!/usr/bin/env python
# coding=utf8

# python 解密日志的脚本

import gzip
try:
  from cStringIO import StringIO
except:
  from StringIO import StringIO
import codecs
import struct
# pip install PyCrypto
from Crypto.Cipher import AES
from optparse import OptionParser


def logan_parse(infile, dst, key, iv):
  '''
  logan 文件解密
  :param infile: 输入文件
  :param dst: 输出文件地址
  :return: NULL
  '''
  dst = open(dst, 'w+')
  with codecs.open(infile, mode='rb') as file:
    # 读取1个字节
    while(file.read(1) == '\x01'):
      # 读取四个字节, 转成int(大端)
      bts = file.read(4)
      print("four bytes: ", [bts])
      size = struct.unpack('>I', bts)[0]
      print("size: ", size)

      # 读取加密内容
      encrypted_content = file.read(size)
      print("encrypted_content: ", [encrypted_content])
      # des 解密
      aes_decryptor = AES.new(key, AES.MODE_CBC, iv)
      decrypted = aes_decryptor.decrypt(encrypted_content)
      print("decrypted_content: ", [decrypted])

      # 读取压缩内容
      compressed_content = decrypted

      # 获取最后一个字节
      last_byte = compressed_content[-1]
      padding_length = struct.unpack('>b', last_byte)[0]
      print("padding_len: ", padding_length)

      # 截取padding之前字节
      compressed_content = compressed_content[0:-padding_length]
      # print ("compressed_content: ", [compressed_content])

      # 解压
      tempIO = StringIO(compressed_content)
      unGzipIO = gzip.GzipFile(mode='rb', fileobj=tempIO)
      decompressed = unGzipIO.read()

      # 写入文件
      print(decompressed)
      dst.write(decompressed)

      # 最后读一个尾巴
      tail = file.read(1)


if __name__ == "__main__":
  arg_parser = OptionParser(
      usage="usage: %prog -i input_path [-o output_path] -k key -v iv"
  )
  arg_parser.add_option("-i", "--input",
                        action="store",
                        type="string",
                        help="input file path")
  arg_parser.add_option("-o", "--output",
                        action="store",
                        type="string",
                        help="output file path")
  arg_parser.add_option("-k", "--key",
                        action="store",
                        type="string",
                        help="aes key")
  arg_parser.add_option("-v", "--iv",
                        action="store",
                        type="string",
                        help="aes iv")
  (options, args) = arg_parser.parse_args()

  input_path = options.input
  key = options.key
  iv = options.iv

  if not input_path or not key or not iv:
    arg_parser.print_help()
    exit(0)

  output_path = options.output
  if not options.output:
    output_path = input_path
    output_path += "_decompressed.txt"

  # 执行解析
  logan_parse(input_path, output_path, key, iv)
