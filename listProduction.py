# -*- coding: UTF-8 -*-

# 列表生成式
# 列表生成式 是python内置的非常简单却强大的可以用来创建list的生成式
# 生成 list [1,2,3,4,5,6,7,8,9,10]   可以用 list(range(1,11))

# 生成【1*1,2*2,3*3,...,10*10】
# 方法一  用循环
L = []
for num in list(range(1,11)):
  L.append(num*num)
print(L)

# 方法二  列表生成式- 一行语句代替循环生成上面的list
[n*n for n in range(1,11)]   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 写列表生成式时，把要生成的元素 n*n 放到前面，后面跟for循环，就可以把list创建出来
# for循环后面还可以加上if判断，这样我们就可以筛选出仅有偶数的平方
[x*x for x in range(1,11) if x%2==0]

# 还可以使用两层循环  可以生成全排列
[m+n for m in 'ABC'  for n in 'XYZ']   # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 三层和三层以上的循环就很少用到了

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
[d for d in os.listdir('.')]   # os.listdir 可以列出文件和目录
# ['.git', '__pycache__', 'fun.py', 'httpTest.py', 'iteration.py', 'learning.py', 'listProduction.py', 'readme.md', 'slice.py', 'test.py']


# for 循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x':'A','y':'B','z':'C'}
for k, v in d.items():
  print(k,'=',v)
# y = B
# x = A
# z = C

# 因此列表生成式也可以使用两个变量来生成list
d = {'x':'A','y':'B','z':'C'}
[k+'='+v for k,v in d.items()]  # ['x=A','y=B','c=Z']

# 把一个list中所有的字符串变成小写的
L = ['Hello','World','IBM','Apple']

[s.lower() for s in L]  # ['hello', 'world', 'ibm', 'apple']

# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁



# 练习
# 在list中即包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
L = ['Hello','World',18,'Apple',None]

# 使用内建的isinstance函数可以判断一个变量是不是字符串
# 请修改列表生成式，通过添加if语句保证列表生成式正确执行


# 我的答案
L2 = [s.lower() for s in L if isinstance(s,str)]  # ['hello', 'world', 'apple']



# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')









