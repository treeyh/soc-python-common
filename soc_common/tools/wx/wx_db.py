# -*- encoding: utf-8 -*-

from pysqlcipher3 import dbapi2 as sqlite


def run():
  wechat_db_decrypt = WechatDatabaseDecrypt()
  wechat_db_decrypt.Init(0x1146340, 0x1131B64)  # 对应 2.6.6.25 版本

  db_filepath = os.path.join(wechat_db_decrypt.GetDatabaseFolder(), "MicroMsg.db")
  key = wechat_db_decrypt.CalculateKey(db_filepath)
  print('key=', key)

  micro_msg_conn = sqlite.connect(db_filepath)
  cur = micro_msg_conn.cursor()
  cur.execute('''PRAGMA key="x'%s'"''' % key)  # 这个也叫 key，那个也叫 key，好麻烦
  cur.execute("PRAGMA cipher_page_size=4096")
  print(cur.execute("select UserName, NickName from Contact").fetchall())


if __name__ == '__main__':
  run()
