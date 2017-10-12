# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/2 18:17"

# 列表常用操作 切片没列
# 创建
list1 = []
list2 = [x*y for x in range(1,5) for y in range(1,x+1) if x!=y]
print('list1: ',list1)
print('list1: ',list2)
#长度
print('list1: ',len(list1))
print('list2: ',len(list2))
# 复制
list1 = list2.copy()
print('list1: ',len(list1))
# 插入数据
list2.insert(2,'insert')
list2.insert(3,'three')
print('list2: ',list2)
# 追加
list1.append('append1')
print('list1: ',list1)
list1.append(list2)
print('list1: ',list1)
list1.extend(list2)
print('list1: ',list1)
# 删除
list1.pop()
print('list1: ',list1)
list1.pop()
print('list1: ',list1)
list1.pop()
print('list1: ',list1)
list2.remove('insert')
print('list2: ',list2)
list2.pop(2)
print('list2: ',list2)
# 查找
print('list1 append1: ',list1.index('append1'))
# 排序
list2.reverse()
print('list2 reverse: ',list2)
list2.sort()
print('list2 sort: ',list2)
# 计数
print('list1 count 2: ',list1.count(2))
# 遍历
for i in list2:
    print('i: ',i)
# 清空
list1.clear()
print('list1: ',list1)
