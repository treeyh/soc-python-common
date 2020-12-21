


def run():
    sql = '''insert into os_order(snb_order_no) values('%(id)d');
insert into os_order_amt (snb_order_no, oem_issue_coupon ) values ('%(id)d', %(id)d);
'''
    ids = ''
    ids1 = ''
    ids2 = ''
    for i in range(1000000101, 1000000600):
        # print(sql % ({'id':i}))
        ids = '''%(ids)s, '%(id)d' ''' % ({'ids':ids, 'id': i})
        ids1 = '''%(ids)s, ('%(id)d') ''' % ({'ids':ids1, 'id': i})
        ids2 = '''%(ids)s, ('%(id)d', %(id)d) ''' % ({'ids':ids2, 'id': i})

    print(ids)
    print('insert into os_order(snb_order_no) values ' + ids1 + ';')
    print('insert into os_order_amt (snb_order_no, oem_issue_coupon ) values ' + ids2 + ';')




if __name__ == '__main__':
    run()
