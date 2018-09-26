#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

#一元二次方程的解法_v0.2
import math

def Error1():
  print('错误1：二次项系数不能为0，请重新输入')

def Error2():
  print('错误2：代尔塔不能小于0，请重新输入')


def Quadratic(a,b,c):
  if a!=0 and (b*b-4*a*c) >= 0:
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return (x1,x2)
  else:
    if a == 0:
      Error1()
    if (b*b-4*a*c) <0:
      Error2()

# a1 = float(input('请输入二次项系数（不能等于0）：'))
# b1 = float(input('请输入一次项系数：'))
# c1 = float(input('请输入常数项：'))

# print(Quadratic(a1,b1,c1))
# print('Done')
# print('')




def g(a,b,c):
  for n in (a,b,c):
    if not isinstance(n,(int,float)):
      raise TypeError('Wrong operand type')
  if b**2 - 4*a*c <0:
    print('方程没有实根')
  else:
    x1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
    if x1 == x2:
      print('方程只有一个实根：x=%.2f' %x1)
    else:
      print('方程的连个实根：x1=%.2f,x2=%.2f' %(x1,x2))

print(g(1,0,-25))



# 计算一个数的任意n次方
def power(x,n=2):
  s = 1
  while n>0:
    n = n-1
    s = s*x
  return s

# power(5)
# power(5,2)


def enroll(name,gender,age=6,city='北京'):
  print(name)
  print(gender)
  print(age)
  print(city)

# enroll('gyy','F')
# enroll('gyy','F',city='nanjing')  # 默认参数可以不按照书序调用，但是当不按顺序提供部分默认参数时，需要把参数名写上






























