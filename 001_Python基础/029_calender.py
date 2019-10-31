import calendar
'''
日历模块
'''

print(calendar.month(2017,7))
'''
     July 2017
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
'''

print(calendar.calendar(2017))

# 闰年返回true
print(calendar.isleap(2000))

# 返回某个月的第一天
# (5, 31)
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30
# 31
print(calendar.monthrange(2017,7))


# 返回某个月每一周的列表
# [[0, 0, 0, 0, 0, 1, 2], [3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30], [31, 0, 0, 0, 0, 0, 0]]
print(calendar.monthcalendar(2017,7))