# -*- coding: UTF-8 -*-

# 返回函数-函数作为返回值

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
# 实现可变参数的求和。通常求和的函数如下定义：

def calc_num(*args):
  ax = 0
  for n in args:
    ax = ax + n
  return ax

# 但是如果不需要立刻求和，而是在后面的代码中，根据需要在计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数

def lazy_sum(*args):
  def sum():
    ax = 0 
    for n in args:
      ax = ax + n 
    return ax
  return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：


# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为‘闭包（closure）’的程序结构拥有极大的威力

# 注意： 当我们调用lazy_sum时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1,2,3)
f2 = lazy_sum(1,2,3)
f1 == f2 # False
# f1 和 f2 的调用结果互不影响



# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 所以，闭包用起来简单，实现起来可不容易

# 另外一个需要注意的问题是，返回的函数并没有立即执行，而是直到调用了f()才执行。

def count():
  fs = []
  for i in range(1,4):
    def f():
      return i*i
    fs.append(f)
  return fs

f1,f2,f3 = count()
# 在上面的例子中，每次循环，都创建可一个新的函数，然后，把创建的3个函数都返回了。
# 你可能认为调用f1(),f2(),f3()结果应该是1，4，9，但实际结果是：f1() 9  f2() 9  f3() 9

# 全都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，他们所引用的变量i已经变成了3，因此最终结果为9.
# ！！！返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办呢？方法是再创建一个函数，用该函数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count_v2():
  def f(j):
    def g():
      return j*j
    return g
  fs = []
  for i in range(1,4):
    fs.append(f(i))   # f(i)立刻被执行，因此i的当前值被传入f()
  return fs
# 再看结果，f1,f2,f3 = count_v2()  f1() 1  f2() 4  f3() 9
# 缺点就是代码较长，可以利用lambda函数缩短代码


# 小结
# 一个函数可以返回一个计算结果，也可以返回一个函数
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量






# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
  def counter():
    return 1
  return counter

#测试
counterA = createCounter()
print(counterA(),counterA(),counterA(),counterA(),counterA())   # 1,2,3,4,5

counterB = createCounter()
if [counterB(),counterB(),counterB(),counterB()] == [1,2,3,4]:
  print('测试通过！')
else:
  print('测试失败！')




def createCounter():
  i = 0
  def counter():
    i = i + 1
    return i
  return counter
counterA = createCounter()
print(counterA(),counterA(),counterA(),counterA(),counterA())



























