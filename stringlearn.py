# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/2 18:17"

# string 常见操作有：
# 复制
a = 'This is letter A'
b = a
print(b)

# 格式化输出
s1 = 'x'
s2 = 'y'
s3 = 'z'
print('%s + %s = %s' %(s1,s2,s3))
print('{0} + {1} = {2}'.format(s1,s2,s3))

# 拼接
t1 = 'Good'
t2 = 'Day!'
t3 = '&&&'
print(t1 + t2)
print(t1.join(t3))
print(t1.join(t2))
print(t2.join(t3))
print(t3.join(t1))

# 排序
print(sorted(['A','a','ADD','aDD','zs','Cr','S']))

# 切片
print( 'This a good day'[1:14])
print( 'This a good day'[:])
print( 'This a good day'[::-1])
print( 'This a good day'[-10::-2])
print( 'This a good day'[-10:-1])
print( 'This a good day'[-10:-1:2])

# ???print( 'This a good day'[-10:-1:-2]) 输出为空
# ???print( 'This a good day'[-1:-10]) 输出为空

# 分割
print( '%%hel%ll%%'.split('%'))

# 索引
print( 'This is a good day!'[10])
print( 'This is a good day!'[18])
print( 'This is a good day!'[-1])

# 查找
print( 'This is a good day!'.index('g'))
print( 'This is a good day!'.index('T'))
print( 'This is a good day!'.find('o'))
print( 'This is a good day!'.find('!'))
print( 'This is a good day!'.find('18'))

# 过滤
print(' hello '.strip())
print('strdelstr'.strip('str'))
print('ml2017'.lstrip('ml'))
print('103zz'.rstrip('zz'))

# 包含
print('A' in('A boy.'))
print('A' not in('A boy.'))
# 长度
print( len('This is a good day!') )

# 大小写转换
ss = 'OH,this is A good day!'
print(ss.upper())
print(ss.lower())
print(ss.swapcase())
print(ss.capitalize())
print(ss.title())

# 计数
print('ssttrpkk'.count('k'))

# 指定长度和两边字符
print('1+2=3'.center(20,'-'))

# 测试
print( 'ADc'.isupper())
print( 'Abc'.istitle())