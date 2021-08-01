from datetime import date
import leancloud

leancloud.init('0vuQYpRkpW8Nf7Ij8kcCyYWG-MdYXbMMI', 'NcQNuz3AKc6Qvgt9npTNdAud')

lines = []

with open('./2010-10.txt', encoding='utf-8') as f:
    lines = f.readlines()


import datetime
Content = leancloud.Object.extend('content')
for line in lines:
    t = line[:len('2020-10-01T12:00:00+08:00')].strip()
    c = line[len('2020-10-01T12:00:00+08:00'):].strip()

    content = Content()
    content.set('createdAt', t)
    content.set('updatedAt', t)
    content.set('content', c)
    content.save()

