# -*- codeing: UTF-8 -*-

# 迭代
# python的for循环抽象程度要高于C的for循环，因为python的for循环不仅可以用在list或tuple上，还可以作用在其他可以迭代的对象上。
# list数据是有下标的，但很多其他数据类型是没有下标的，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代

d = {'a':1, 'b':2, 'c':3}
for key in d :
  print(key)  # a c b 

#之所以是 a c b ，dic的存储不是按照list的方式顺序排列，所以迭代出的结果顺序很可能不一样
# 默认情况下，dict迭代的是key，
# 如果要迭代value,可以用  for value in d.values()
# 如果要同时迭代key和value，可以用 for k,v in d.items()

for key,value in d.items():
  print(key,value)


# 字符串也是可以迭代对象，也可以用for循环
for ch in 'ABC':
  print(ch)

# 在python中，当使用for循环时，只要作用一个可迭代对象，for循环都可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型

# 判断一个对象时可迭代对象： 方法是通过 collections模块的Iterable类型判断
from collections import Iterable
isinstance('abc',Iterable)  # True   判断 str 是否可迭代
isinstance([1,2,3],Iterable)  # True 判断 list 是否可迭代
isinstance(123,Iterable)  # False  判断整数是否可迭代



# 如果要对list实现 类似 java 那样的下标循环  python内置的 enumerate 函数可以把一个list变成索引-元素对
# 这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(['A','B','C']):
  print(i,value)
# 0 A
# 1 B 
# 2 C

# 上面的循环里同时引用了两个变量，在python里很常见，如
for x,y in [(1,1),(2,4),(3,9)]:
  print(x,y)
# 1 1
# 2 4
# 3 9




# 练习
# 使用迭代 查找一个list钟最小和最大值，并返回一个tuple
def findMinAndMax(L):
  if len(L) == 0:
    return (None,None)
  min = L[0]
  max = L[0]
  for num in L:
    if num < min:
      min = num
    if num > max:
      max = num
  return (min,max)
  


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')












