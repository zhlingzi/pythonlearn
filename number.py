# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/2 18:17"

# a+b addition
#add = lambda a,b: print('The result of',a,'+',b,'=', a+b)
add = lambda a,b: a+b
# a-b subtraction
sub = lambda a,b: print('The result of',a,'-',b,'=', a-b)
# a*b multiplication
mul = lambda a,b: print('The result of',a,'*',b,'=', a*b)
# a/b division
div = lambda a,b: print('The result of',a,'*',b,'=', a/b)
# a//b quotient
quo = lambda a,b: print('The result of',a,'*',b,'=', a//b)
# a%b remainder
rem = lambda a,b: print('The result of',a,'*',b,'=', a%b)
# |a| absolute value
abso = lambda a: print('The result of |',a,'| =', abs(a))
# a**n power
#pow = lambda a,n: print('The result of',a,'^',n,'=', a**n)
pow = lambda a,n: a**n
# fibonacc
def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

if __name__ == '__main__':
    add(2.1,3)
    sub(2,5)
    mul(4,6)
    mul(3.4,7.2)
    div(3,5)
    div(6.2,3.1)
    quo(3, 5)
    rem(3, 5)
    quo(6.2, 3.1)
    rem(6.2,3.1)
    abso(-8.5)
    pow(2,3)
    pow(2,8)
    fibo(2000)

