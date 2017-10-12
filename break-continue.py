# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/2 18:21"

# break or continue or return
def print_number():
   while True:
       for i in range(100):
           if  i % 2  == 0:
               continue
           elif i == 65:
               break
           print(i,end= ' ')
       print('break')
       return

print_number()
