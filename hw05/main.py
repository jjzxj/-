import re
line='''我的电子邮件是tom@gmail.com。
将什么发送到jerry123@163.com或者3123432@qq.com.
若遇特殊情况打电话给182123445678'''
a=re.search(r'[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+',line,re.A)
print('邮箱1: ',a)
b=re.search(r'[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*@?163.com',line,re.A)
print('邮箱2: ',b)
c=re.search(r'[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*@?qq.com',line,re.A)
print('邮箱3: ',c)
d=re.search(r'(\d+){12}',line)
print('电话号码: ',d)
