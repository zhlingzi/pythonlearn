# -*- coding:utf8 -*-
''' Create on "2017/10/5 7:55"
    _author_="zhao ling"
    Poject: 《byte of python》

# Exception 异常
# try 尝试 except 处理异常 raise举起(抛出)
# 将所有可能引发错误或异常的语句放在 try 中
# 并将相应的错误或异常处理器(handler)放在 except 中
  else 在没有捕获异常时执行
 '''

try:
    text = input('Enter the text:')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('Your entered {}'.format(text))

