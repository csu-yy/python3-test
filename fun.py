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


# 默认参数
def enroll(name,gender,age=6,city='北京'):
  print(name)
  print(gender)
  print(age)
  print(city)

# enroll('gyy','F')
# enroll('gyy','F',city='nanjing')  # 默认参数可以不按照书序调用，但是当不按顺序提供部分默认参数时，需要把参数名写上




# 注意 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 如下  第一次调用 add_End() 输出 ['END']  但是第二次调用 则 输出 ['END','END'] 后面也是
def add_End(l=[]):
  l.append('END')
  return l


# 要修改上面的例子，我们可以用None这个不变对象来实现：
def add_End_v2(l=None):
  if l is None:
    l = []
  else:
    l.append('END')
  return l



# 可变参数
def calc(numbers):
  s = 0
  for n in numbers:
    s = s + n*n
  return s

# 由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
# 但是调用的时候，需要先组装出一个list或tuple：
# calc([1,2,3])
# calc((1,3,5,7))


# 更改上面calc参数为可变参数 如下
def calc_v2(*numbers):
  s = 0
  for n in numbers:
    s = s + n*n
  return s
# 调用该函数时，可以传入任意个参数，包括0个参数  如 calc(1,2,3)  不必一定要组装成list或者tuple

nums = [1,2,3]
print(calc_v2(nums[0],nums[1],nums[2]))
#这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
print(calc_v2(*nums))


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def person(name,age,**kw):
  print('name:',name,'age:',age,'other:',kw)

print(person('Jack',24,city='Beijing',job='Engineer'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))

# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
def person2(name,age,**kw):
  if 'city' in kw:
    # 有 city 参数
    pass
  if 'job' in kw:
    # 有job 参数
    pass



# 命名关键字参数
# 如果要限制关键字参数的名字， 就可以使用命名关键字参数
# 例如 只接收 ‘city’和‘job’ 作为关键字参数，则函数定义如下
def person(name,age,*,city,job):
  print(name,age,city,job)

# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 和关键字参数**kw不同，命名关键字参数需要一个特殊的分隔符
# 调用方式  person('Jack', 24, city='Beijing', job='Engineer')
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：如 person('Jack', 24, 'Beijing', 'Engineer')



# 如果函数定义中已经有一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
  print(name,age,args,city,job)




# 参数组合
# 函数中，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数。5种参数可以组合使用。
# 但注意：参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a,b,c=0,*args,**kw):
  print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
  print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)




# 总结
# 必选函数：
#         定义：func1(a,b)
#         调用：func1(1,2)
# 默认参数：
#         定义：func2(a,b,c=3)
#         调用：func2(1,2) ; func2(1,2,5)
# 可变参数：
#         定义：func3(a,b,*list1)
#         调用：list2=[3,4,5] func3(1,2,*list2) ; func3(1,2,3,4,5)
# 关键字参数：
#         定义：func4(a,b,**dict1)
#         调用：dict2={'key':'key','word':'word'} func4(1,2,**dict2) ; func4(1,2,aa='key',bb='word')
# 命名关键字参数：
#         定义：func5(a,b,*,c,d)
#         调用：dict={'c':'c','d':'d'} func5(1,2,**dict) ; func5(1,2,c='3',d='4')
# 命名关键字参数与可变参数同时存在：
#         定义：func6(a,b,*c,d,e)
#         调用：func6(1,2,d='4',e='5') ; func6(1,2,'333',d='4',e='5')
#             dict1={'d':'4','e':'5'} func6(1,2,**dict1) ; dict1={'d':'4','e':'5'} func6(1,2,**dict1)


# 练习题 product 函数允许计算两个数的乘积，稍加改造，变成可接受一个或多个数并计算乘积
def product(x, y):
    return x * y

# 我的答案
def product2(x,y=1,*numbers):
  s = 1
  for num in numbers:
    s = s * num

  return x*y*s



# 递归函数
# 计算阶乘
def fact(n):
  if n == 1:
    return 1
  return n * fact(n-1)







