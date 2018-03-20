import codecs
import time
import os
import datetime

my_name = '唐庆昌'
dir = 'diary'

month = int(time.strftime("%m"))
day = int(time.strftime("%d"))
year = int(time.strftime("%Y"))

file_base_name = "{y}年{m}月{d}-{n}.txt".format(
    y=year, m=month, d=day, n=my_name)

path = dir + '/' + file_base_name

if not os.path.exists(path):
    file = codecs.open(path, 'w+', encoding='utf-8')
else:
    file = codecs.open(path, 'r+', encoding='utf-8')

tomorrow = datetime.date(year, month, day) + datetime.timedelta(1)

tomorrow_month = int(tomorrow.strftime("%m"))
tomorrow_day = int(tomorrow.strftime("%d"))

template_file = codecs.open("./conf/template.txt", encoding='utf-8')
data = template_file.read()

file.seek(0)
file.truncate()
file.write(data.format(m=month, d=day, tm=tomorrow_month,
                       td=tomorrow_day, n=my_name))

file.close()
template_file.close()
print("generated success: " + path)
