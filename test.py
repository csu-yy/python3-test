#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

def clear():
  os.system('clear')

print (u'中文测试正常')

test = 'hello, %s' %('world')
print(test)

test2 = 'Hi, %s,you have $%d'  %('gyy', 10000000)
print(test2)

s1 = 72
s2 = 85
s3 = s1/s2
test3 = '%.1f' %(s3*100)
print(test3)

r = (s1/s2)*100
print('%.1f' % r)


# 数组 list
a1 = ['chi','iio','po']
print(a1)

a1.insert(1,'gyy')
print(a1)


age = 18
if age >= 18:
  print(1)
else:
  print(2)


# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#   print('00前')
# else:
#   print('00后')



height = 1.75
weight = 80.5
bmi = weight/(height* height)
print(bmi)
if bmi<18.5:
  print('过轻')
elif bmi>=18.5 and bmi<25:
  print('正常')
elif bmi>=25 and bmi<28:
  print('过重')
elif bmi>=28 and bmi<32:
  print('配胖')
elif bmi>32:
  print('严重肥胖')



# 计算 0-100的加和
sum = 0
for x in list(range(101)):
  sum = sum + x

print(sum)


# 计算100以为的所有奇数之和
sum = 0
n = 99
while n > 0:
  sum = sum + n
  n = n - 2
print(sum)




n = 1
while n<=100:
  if n > 10:
    break
  print(n)
  n = n + 1
print('END')


n = 0
while  n<10:
  n = n+1
  print(n)


n = 0 
while n < 10:
  n = n + 1
  if n % 2 == 0:  # 如果n是偶数，执行continue语句
    continue       # continue语句会直接继续下一轮循环，后续的print()语句不会执行
  print(n)



# 函数
def my_abs(x):
  if not isinstance(x, (int, float)):
    raise TypeError('bad operand type')
  if x>0:
    return x
  else:
    return -x

print(my_abs(-99))



def nop():
  pass


import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
