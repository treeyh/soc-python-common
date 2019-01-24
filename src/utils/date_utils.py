# -*- encoding: utf-8 -*-


from datetime import date, datetime, timedelta
import time

_arrow_type = True
try:
    import arrow
except Exception as e:
    _arrow_type = False


# dt = datetime.strptime(string, "%Y-%m-%d.%H:%M:%S.%f")


def str_to_time(strtime):
    t_tuple = time.strptime(strtime, "%Y-%m-%d %H:%M:%S")
    return time.mktime(t_tuple)


def str_to_time2(strtime):
    dt = datetime.strptime(strtime, "%Y-%m-%d %H:%M:%S")
    t_tuple = dt.timetuple()
    return time.mktime(t_tuple)


def datetime_now_diff(datetimestr):
    '''
        给入的时间字符串，如当前时刻的差值（秒）
    '''
    t_tuple = time.strptime(datetimestr, "%Y-%m-%d %H:%M:%S")
    diff = time.mktime(t_tuple) - time.time()
    return diff


def get_datetimestr_by_time(t):
    return datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')


def get_now_datetimestr2():
    return datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


def get_now_datetimestr3():
    return datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')


def get_now_datestr():
    return add_datetime_by_now(days=0).strftime('%Y-%m-%d')


def get_now_datestr2():
    return add_datetime_by_now(days=0).strftime('%Y%m%d')


def get_now_datetimestr():
    return add_datetime_by_now(days=0).strftime('%Y-%m-%d %H:%M:%S')


def get_datetimestr(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def get_datetimestr2(dt):
    return dt.strftime('%Y%m%d%H%M%S')


def get_datetimestr3(dt):
    return dt.strftime('%Y-%m-%d')


def get_datetimestr4(dt):
    return dt.strftime('%Y%m%d')


def get_add_datest(days):
    return add_datetime_by_now(days=days).strftime('%Y-%m-%d')


def get_add_datest2(days):
    return add_datetime_by_now(days=days).strftime('%Y%m%d')


def get_add_datehstr(days):
    return add_datetime_by_now(days=days).strftime('%Y%m%d%H')


def get_add_datetimestr(days):
    return add_datetime_by_now(days=days).strftime('%Y-%m-%d %H:%M:%S')


def date_string_to_datetime(string):
    return datetime.strptime(string, "%Y-%m-%d")


def date_string_to_datetime2(string):
    return datetime.strptime(string, "%Y%m%d")


def date_string_to_datetime3(string):
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S")


def date_string_to_datetime4(string):
    return datetime.strptime(string, "%Y%m%d%H%M%S")


def datetime_to_str(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def datetime_to_time(dt):
    return time.mktime(dt.timetuple())


def str_to_time(string):
    return time.mktime(datetime.strptime(string, '%Y-%m-%d %H:%M:%S').timetuple())


def add_datetime_by_now(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
    return add_datetime_by_datetime(days=days, seconds=seconds, microseconds=microseconds,
                                    milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks)


def add_datetime_by_datetime(dt=datetime.now(), days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0,
                             weeks=0):
    return dt + timedelta(days=days, seconds=seconds, microseconds=microseconds,
                          milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks)


def str_is_date(string):
    '''判断是否是一个有效的日期字符串'''
    try:
        time.strptime(string, '%Y%m%d')
        return True
    except:
        return False


def sleep(second):
    time.sleep(second)


if __name__ == '__main__':
    # print(datetime.fromtimestamp(1473312015).strftime('%Y-%m-%d %H:%M:%S'))
    # print(datetime.fromtimestamp(1472390999).strftime('%Y-%m-%d %H:%M:%S'))
    # print(str_to_time2("2016-02-07 21:44:36"))
    # print(1473312015 - time.time())
    # print(1473311912 - time.time())
    #
    # print(datetime.fromtimestamp(1473552004).strftime('%Y-%m-%d %H:%M:%S'))
    # print(1473552004 / 300)
    # print(4911841 % 864)
    # print(1473552004 / 300 % 864)
    #
    # print(datetime_to_time(datetime.now()))

    print(str_to_time2("2018-07-01 00:00:00"))

    # if True == _arrow_type:
    #     import sys
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.now())
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.now().replace(hours=-1, weeks=+3))
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.utcnow())
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.get('2015-12-22T10:45:29.742000+08:00'))
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.get('2015-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss'))
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.get(1450753884.9))
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.get('1450753884.9'))
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.now().timestamp)
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.now().float_timestamp)
    #     print '%d : %s' % (sys._getframe().f_lineno, type(arrow.Arrow.now().naive))
    #     print '%d : %s' % (sys._getframe().f_lineno, type(arrow.Arrow.now().date()))
    #     print '%d : %s' % (sys._getframe().f_lineno, type(arrow.Arrow.now().time()))
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.now().format())
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.now().format('YYYY-MM-DD HH:mm:ss ZZ'))
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.now().humanize())

    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.fromtimestamp(time.time()))
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.fromdatetime(datetime.now()))
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.fromdate(date(2012, 12, 3)))

    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.strptime('2015-05-05 12:30:45', '%Y-%m-%d %H:%M:%S'))
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.strptime('2015-05-05 12:30:45', '%Y-%m-%d %H:%M:%S'))

    #     start = datetime(2013, 5, 5, 12, 30)
    #     end = datetime(2013, 5, 5, 17, 15)
    #     for r in arrow.Arrow.range('hour', start, end):
    #         print r

    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.now().span('day'))
    #     start = datetime(2013, 5, 5, 12, 30)
    #     end = datetime(2013, 5, 5, 17, 15)
    #     for r in arrow.Arrow.span_range('hour', start, end):
    #         print r

    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.now().floor('hour'))
    #     print '%d : %s' % (sys._getframe().f_lineno, arrow.Arrow.now().ceil('hour'))
    #     print time.time()