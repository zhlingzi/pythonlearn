# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/2 18:18"

# 集合
# 创建
seta = {1,2,1,2,3,4,5,6,6,6,6}
setb = set()
print('seta : ',seta)
print('setb : ',setb)
# 添加
seta.add('hello')
setb.add('hello')
print('seta : ',seta)
print('setb : ',setb)
seta.update([22,3,33,4445])
setb.update([2,3,33,4445,6])
print('seta : ',seta)
print('setb : ',setb)
# 删除
seta.pop()
print('seta : ',seta)
seta.remove(6)
print('seta : ',seta)
# 交集
print('交集 ： ',seta.intersection(setb))
# 并集
print('并集 ： ',seta.union(setb))
# 差集
print('差集 ： ',seta.difference(setb))
# 清空
seta.clear()
print('seta : ',seta)

