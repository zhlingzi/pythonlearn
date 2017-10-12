# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/2 18:18"

# 字典
# 创建
dict1 = {'one':'a', 'two': 2, 'three': '3c', 'four': '4f', 'five': 5}
dict2 = dict(spam = 11, spam2 = 22)
print('dict1 : ',dict1)
print('dict2 : ',dict2)
# 访问值
print('dict1[one] : ',dict1['one'])
# 遍历
print('the key in dict1 : ',end=' ')
for k in dict1.keys():
    print(k,end=' ')
print()
print('the value in dict1 : ',end=' ')
for v in dict1.values():
    print(v,end= ' ')
print()
print('the key-value in dict1 : ')
for key,value in dict1.items():
    print(key,value)

print('the index-key in dict1 : ')
for i,k in enumerate(dict1):
    print(i,k)
# 修改
dict2['spam'] = 's'
print('dict2 : ',dict2)
# 更新
dict2.update(update = 3)
print('dict2 : ',dict2)
# 删除
del dict2['spam2']
print('dict2 : ',dict2)
# 特性1：键不能重复，如果赋值是键出现两次，记住后一次赋的值
dict3 = {'33': 3, '44': 4, '44': 6}
print('dict3 : ',dict3)
# 特性2：键不可变
dict4 = {(1,2,3):2, 'a':3, 1:4}
print('dict4 : ',dict4)
