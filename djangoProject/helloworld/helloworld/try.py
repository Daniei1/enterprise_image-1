import re

time = '浙江利豪家具有限公司成立于1999年，1998年7月6日'
r2 = r'(\d+)年(\d+)月(\d+)日|(\d+)年(\d+)月|(\d{4})年'
# 时间上的问题可以有好多种，有的是“一九九0年四月九日”，既涉及到文字表示的又有数字表示的时间，所以有四位的时间就提取
r3 = r'.{4}年.{1,2}月.{1,2}日|.{4}年.{1,2}月|.{4}年'
return_time = ''
if re.search(r2, time) != None:
    return_time = return_time + re.search(r2, time).group()
elif re.search(r3, time) != None:
    return_time = return_time + re.search(r3, time).group()
print(return_time)