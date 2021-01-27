


def run():
    sql = '''insert into os_order(snb_order_no) values('%(id)d');
insert into os_order_amt (snb_order_no, oem_issue_coupon ) values ('%(id)d', %(id)d);
'''
    ids = ''
    ids1 = ''
    ids2 = ''
    for i in range(100000001, 100000002):
        # print(sql % ({'id':i}))
        if ids == '':
            ids = ''''%(id)d' ''' % ({'ids':ids, 'id': i})
            ids1 = '''('%(id)d') ''' % ({'ids':ids1, 'id': i})
            ids2 = '''('%(id)d', %(id)d) ''' % ({'ids':ids2, 'id': i})
        else:
            ids = '''%(ids)s, '%(id)d' ''' % ({'ids':ids, 'id': i})
            ids1 = '''%(ids)s, ('%(id)d') ''' % ({'ids':ids1, 'id': i})
            ids2 = '''%(ids)s, ('%(id)d', %(id)d) ''' % ({'ids':ids2, 'id': i})

    print(ids)
    print('insert into os_order(snb_order_no) values ' + ids1 + ';')
    print('insert into os_order_amt (snb_order_no, oem_issue_coupon ) values ' + ids2 + ';')


# insert into os_order(snb_order_no) values('1000000101');
# insert into os_order_amt (snb_order_no, oem_issue_coupon ) values ('1000000101', 1000000101);
# delete from `os_order_amt` where `snb_order_no` in ('1000000001');
# delete from `os_order` where  `snb_order_no` in ('1000000001');




if __name__ == '__main__':
    run()
