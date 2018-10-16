# -*- coding: UTF-8 -*-

# 生成器
# 列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在python中，这种一边循环一遍计算的机制，称为生成器：generator

# 因为 之前通过列表生成式，可以直接创建一个list。但受到内存的限制，列表容量有限。
# 而且创建一个包含一个100万个元素的列表，不仅占用恨到的存储空间，如果我们仅仅需要访问前面的几个元素，那后面绝大多数元素占用的空间都白白浪费了。

# 创建generator的方法
# 法一： 只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x*x for x in range(10)] # 列表生成式  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x*x for x in range(10)) # 生成器     <generator object <genexpr> at 0x1102c9c78>

# list可以直接打印出每一个元素，但generator如何打印出每个元素呢？
# 用 next() 函数获得generator的下一个返回值
next(g)  # 一直调用后  会相继输出 0, 1, 4, 9, 16, 25, 36, 49, 64, 81  

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素
# 没有更多的元素时，抛出 StopIteration 的错误

# 当然上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator是可迭代对象
g = (x*x for x in range(10))
for n in g:
  print(n)
# 0, 1, 4, 9, 16, 25, 36, 49, 64, 81

# 所以我们创建了一个generator后，基本上永远也不会调用next(),而是通过for循环来迭代它。并且不关心 StopIteration 的错误



# 法二：函数
# 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
# 以 著名的斐波拉契数列(Fibonacci)，除第一个和第二个数外，任意一个数都可由前两个数相加得到
# 1,1,2,3,5,8,13,21,34,...

# 输出斐波那契数列的前N个数
def fib(max):
  n,a,b = 0,0,1
  while n < max:
    print(b)
    a, b = b, a+b
    n = n + 1
  return 'done'

# 注意赋值语句： a, b = b, a+b  相当于

# t = (b,a+b)  # t 是一个tuple
# a = t[0]
# b = t[1]

# 不必显示写出临时变量t就可以赋值

# 实际上，fib函数定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator
# 也就是说上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改成yeild b 就可以了

def fibGenerator(max):
  n,a,b = 0,0,1
  while n<max:
    yield b
    a,b = b, a+b
    n = n + 1
  return 'done'
# fibGenerator 就是定义 generator 的另一种方法。如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个generator
fibGenerator(6)  # <generator object fibGenerator at 0x104476048>


# 这里，最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用 next() 的时候执行，遇到 yield 语句返回，在执行时从上次返回的 yield 语句处继续执行


# 举个简单的例子，定义一个generator，依次返回数字1，3，5
def odd():
  print('step1')
  yield 1
  print('step2')
  yield(3)
  print('step3')
  yield(5)
# 调用该 generator 时，首先要生成一个 generator 对象，然后利用 next() 函数不断获得下一个返回值
o = odd()
next(o)  # step1 1
next(o)  # step2 3
next(o)  # step3 5
# next(o)  # 报错  StopIteration

# 可以看到，odd 不是普通函数，而是 generator ，在执行过程中，遇到 yield 就中断。
# 执行三次 yield 后，已经没有 yield 可以执行了。所以第4次调用 next(o) 就报错

# 回到 fibGenerator 函数，在循环中不断调用yield，就会不断中断，当然要给循环设置一个条件跳出循环，不然就会生成一个无限序列

# 把函数设置成 generator 后，基本上从来不会用 next() 来获取下一个返回值，而是用 for 循环来替代 

for n in fibGenerator(6):
  print(n)
# 1, 1, 2, 3, 5, 8

[x for x in fibGenerator(6)]  # [1, 1, 2, 3, 5, 8]

# 但是用 for 循环，发现拿不到 generator 中return语句的返回值，若想拿到，需捕获StopIteration错误，该返回值包含在StopIteration的value中
g = fibGenerator(6)
while True:
  try:
    x = next(g)
    print('g:',x)
  except StopIteration as e:
    print('Generator return value:',e.value)
    break
# g:1 g:1 g:2 g:3 g:5 g:8   Generator return value: done




# generator 是非常强大的工具，在python 中，可以简单地把列表生成式改成 generator，也可以通过函数实现复杂逻辑的generator
# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的 generator 来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

# 注意区分普通函数和generator函数，普通函数调用直接返回结果，generator函数的‘调用’实际返回一个generator对象













# 练习
# 杨辉三角形的定义如下
 #           1
 #          / \
 #         1   1
 #        / \ / \
 #       1   2   1
 #      / \ / \ / \
 #     1   3   3   1
 #    / \ / \ / \ / \
 #   1   4   6   4   1
 #  / \ / \ / \ / \ / \
 # 1   5   10  10  5   1

# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

def triangles():
  pass




# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
  print(t)
  results.append(t)
  n = n + 1
  if n == 10:
    break
if results == [
  [1],
  [1, 1],
  [1, 2, 1],
  [1, 3, 3, 1],
  [1, 4, 6, 4, 1],
  [1, 5, 10, 10, 5, 1],
  [1, 6, 15, 20, 15, 6, 1],
  [1, 7, 21, 35, 35, 21, 7, 1],
  [1, 8, 28, 56, 70, 56, 28, 8, 1],
  [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
  print('测试通过!')
else:
  print('测试失败!')













