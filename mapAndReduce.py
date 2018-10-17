# -*- coding: UTF-8 -*-

# map/reduce
# python内建了map()和reduce()函数。

# map
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# 举例说明，比如我们有一个函数 f(x)=x*x，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：

def f(x):
  return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
list(r)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

# map()作为高阶函数，事实上它把运算规则抽象了，
# 因此，我们不但可以计算简单的f(x)=x*x，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
list(map(str,[1,2,3,4,5,6,7,8,9])) # ['1', '2', '3', '4', '5', '6', '7', '8', '9']




# reduce
# reduce 的用法：
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

# 比方对一个序列求和，就可以用reduce实现
from functools import reduce
def add(x,y):
  return x+y

reduce(add,[1,3,5,7,9])
# 当然求和运算可以直接用ppython内置函数sum()，没必要动用reduce

# 但是如果把序列[1，3，5，7，9]变换成整数13579，reduce就可以排上用场
from functools import reduce
def fn(x,y):
  return x*10+y

reduce(fn,[1,3,5,7,9])  # 13579
# 这个例子没有多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数

from functools import reduce
def fn(x,y):
  return x*10+y
def char2num(s):
  digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
  return digits[s]
reduce(fn,map(char2num,'13579'))


# 整理成一个str2int的函数就是：
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
  def fn(x, y):
    return x * 10 + y
  def char2num(s):
    return DIGITS[s]
  return reduce(fn, map(char2num, s))

str2int('13579')  # 135


# 还可以用lambda函数进一步简化成：
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2num(s):
  return DIGITS[s]
def str2int(s):
  return reduce(lambda x, y: x * 10 + y, map(char2num,s))
# 也就是说，假设python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码






# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    pass
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 我的答案
def normalize(name):
  return name[0].upper() + name[1:].lower()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)



# 练习
# python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list兵利用reduce求积：
def prod(L):
  pass

# 测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 我的答案
def prod(L):
  def innerProd(n1, n2):
    return n1 * n2
  return reduce(innerProd, L)
# 测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



# 练习
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# def str2float(s):
#   pass
# # 测试
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')



def str2float(s):
  def fn(x,y):
    return x * 10 + y
  n = s.index('.')
  s1 = list(map(int,[x for x in s[:n]]))
  s2 = list(map(int,[x for x in s[n+1:]]))
  return reduce(fn,s1) + reduce(fn,s2)/10**len(s2)   # m**n 这个表达的就是 m 的 n 次方

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


























