#-*- encoding: utf-8 -*-

import os
import sys
import time

# from kafka import KafkaProducer
from kafka import SimpleProducer, SimpleClient, KafkaProducer, SimpleConsumer

path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..')

from helper import str_helper, file_helper, date_helper, sys_helper




def add_queue(dt):

    client = SimpleClient('10.10.1.71:9092')
    # client = SimpleClient('192.168.1.151:9092')
    producer = SimpleProducer(client, async=True)

    for i in range(100):
        producer.send_messages('my-topic', 'msg:'+dt+':'+str(i))
        print i

    # producer.flush()



def read_queue():
    client = SimpleClient('10.10.1.71:9092')
    # client = SimpleClient('192.168.1.151:9092')
    consumer = SimpleConsumer(client, "tree", "tree")
    for message in consumer:
        # message is raw byte string -- decode if necessary!
        # e.g., for unicode: `message.decode('utf-8')`
        print(message)
        # print(message.offset)
        # print(message.message.value)




if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print 'begin'
    dt = date_helper.get_now_datetimestr3()
    # add_queue(dt)
    read_queue()
    print 'end'