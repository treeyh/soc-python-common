#-*- encoding: utf-8 -*-


from elasticsearch import Elasticsearch
from elasticsearch import helpers



def build_order_body(index, start):
  orders = []

  for i in range(start, start + 500):
    id = str(i)
    order_index = {
      '_op_type': 'index',
      '_index': index,
      '_id' : id,
      '_source': {
          "id": id,
          "snb_order_no": "snb_order_no_"+id,
          "cplc": "cplc",
          "device_vendor": "device_vendor",
          "device_model": "device_model",
          "device_unicode": "device_unicode",
          "snb_account_id": "snb_account_id_"+id,
          "payment_channel": "payment_channel",
          "app_code": "app_code",
          "instance_id": "instance_id",
          "sp_id": "sp_id",
          "should_deduct_amt": i,
          "real_deduct_amt": i,
          "normal_issue_card_amt": i,
          "activity_issue_card_amt": i,
          "normal_recharge_amt": i,
          "activity_recharge_amt": i,
          "transaction_code": "transaction_code_"+id,
          "card_no": "card_no_"+id,
          "pay_serial_no": "pay_serial_no_"+id,
          "third_order_no": "third_order_no_"+id,
          "pay_status": 1,
          "order_type": 1,
          "card_operate_status": 1,
          "recharge_status": 1,
          "activity_flag": 1,
          "create_time": i,
          "update_time": i,
          "order_status": 1,
          "row_status": 1,
          "pay_time": i,
          "expire_time": i,
          "receive_coupon": i,
          "oem_issue_coupon": i,
          "oem_recharge_coupon": 1,
          "refund_coupon": i,
          "before_recharge_amt": i,
          "business_complete_time": "2020-12-03T12:00:12Z",
          "is_new_future": 1,
          "not_oem_snb_user_id": "not_oem_snb_user_id_"+id,
          "channel_type": "Alipay"
      }
    }
    orders.append(order_index)
  return orders



def es_run():
  index = 'order_index'
  es = Elasticsearch(["10.0.54.105"], port="9200")
  res = es.exists(index=index, id=1)
  print(res)

  for i in range(3233001, 30000000, 500):
    orders = build_order_body(index, i)
    helpers.bulk(es, orders)
    print(str(i))

  # res = es.indices.get_mapping()
  # print(res)


if __name__ == "__main__":
    es_run()