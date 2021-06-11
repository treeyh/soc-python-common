# -*- encoding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText


def send_mail(user, postfix, password, smtphost, to_list, cc_list=None, bcc_list=None, sub='', content='', subtype='plain', charset='UTF-8'):
  '''
      发送文本邮件，参考：http://www.cnblogs.com/xiaowuyi/archive/2012/03/17/2404015.html
      user：发送用户名，@之前的字符
      postfix：发送邮箱后缀，@之后的字符
      password：邮箱密码
      smtphost：smtp域名
      to_list：发送目标邮箱，list
      cc_list：抄送目标邮箱，list
      bcc_list：追加目标邮箱，list
      sub：邮件标题
      content：邮件内容
      subtype：邮件类型，文本使用plain，html使用html
      charset：字符编码，默认UTF-8
  '''
  me = user + "<" + user + "@" + postfix + ">"
  msg = MIMEText(content, _subtype=subtype, _charset=charset)
  msg['Subject'] = sub
  msg['From'] = me
  msg['To'] = ";".join(to_list)
  if None != cc_list and len(cc_list) > 0:
    to_list.extend(cc_list)
    msg['Cc'] = ";".join(cc_list)
  if None != bcc_list and len(bcc_list) > 0:
    to_list.extend(bcc_list)
    msg['Bcc'] = ";".join(bcc_list)

  try:
    server = smtplib.SMTP()
    server.connect(smtphost)
    server.login(user, password)
    server.sendmail(me, to_list, msg.as_string())
    server.close()
    return True
  except Exception as e:
    print(str(e))
    return False


if __name__ == '__main__':
  user = 'treeyh01'
  postfix = '126.com'
  password = '55555'
  smtphost = 'smtp.126.com'
  to_list = ['yuhai@tv189.com']
  cc_list = []
  bcc_list = []
  sub = '12上海3'
  content = 'ab上海c'

  send_mail(user, postfix, password, smtphost, to_list, cc_list, bcc_list, sub, content)
