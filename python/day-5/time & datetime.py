import time
'''
time

>>> time.clock()
0.137564


>>> time.ctime()
'Thu Sep 14 10:22:16 2017'


>>> time.gmtime()
time.struct_time(tm_year=2017, tm_mon=9, tm_mday=14, tm_hour=2, tm_min=22, tm_sec=24, tm_wday=3, tm_yday=257, tm_isdst=0)

>>> time.ctime(time.time()-86640)
'Wed Sep 13 10:18:41 2017'


>>> time.localtime()
time.struct_time(tm_year=2017, tm_mon=9, tm_mday=14, tm_hour=10, tm_min=23, tm_sec=53, tm_wday=3, tm_yday=257, tm_isdst=0)
>>> time.localtime(time.time()+86440)
time.struct_time(tm_year=2017, tm_mon=9, tm_mday=15, tm_hour=10, tm_min=25, tm_sec=26, tm_wday=4, tm_yday=258, tm_isdst=0)


>>> time.mktime(time.gmtime())
1505327581.0

>>> time.gmtime()
time.struct_time(tm_year=2017, tm_mon=9, tm_mday=14, tm_hour=2, tm_min=32, tm_sec=35, tm_wday=3, tm_yday=257, tm_isdst=0)
>>> time.ctime()
'Thu Sep 14 10:32:46 2017'






datetime
>>> datetime.datetime.now()
datetime.datetime(2017, 9, 14, 10, 45, 8, 770722)
>>> datetime.datetime.now().timetuple()
time.struct_time(tm_year=2017, tm_mon=9, tm_mday=14, tm_hour=10, tm_min=45, tm_sec=31, tm_wday=3, tm_yday=257, tm_isdst=-1)
>>> time.mktime(datetime.datetime.now().timetuple())
1505357167.0

>>> datetime.date.today()
datetime.date(2017, 9, 14)

>>> datetime.date.fromtimestamp(time.time())
datetime.date(2017, 9, 14)
>>> datetime.date.fromtimestamp(time.time()-86440)
datetime.date(2017, 9, 13)

>>> datetime.date.today()
datetime.date(2017, 9, 14)


'''