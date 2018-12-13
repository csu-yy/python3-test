# -*- coding: UTF-8 -*-

# 装饰器

# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数

def now():
  print('2018-11-22')

f = now
f()  # 2018-11-22

# 函数对象有一个__name__属性，可以拿到函数的名字：
now.__name__  # 'now'
f.__name__   # 'now'

# 现在，假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

# 本质上，decorator就是一个返回函数的高阶函数。
# 所以，我们要定义一个能打印日志的高阶decorator。可以定义如下：

def log(func):
  def wrapper(*args,**kw):
    print('call %s():' % func.__name__)
    return func(*args,**kw)
  return wrapper
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助python的@语法，把decorator置于函数的定义处：

@log
def now():
  print('2018-11-23')

# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
now() # call now():  2018-11-23

# 把@log 放到 now() 函数的定义处，相当于执行了语句： now = log(now)
# 由于 log() 是一个decorator，返回一个函数，所以，原来的now()函数仍存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数

# wrapper()函数的参数定义是(*args,**kw),因此，wrapper()函数可以接受任意参数的调用。
# 在wrapper函数内，首先打印日志，再紧接着调用原始函数。



# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如：
def log(text):
  def decorator(func):
    def wrapper(*args,**kw):
      print('%s %s():' % (text,func.__name__))
      return func(*args,**kw)
    return wrapper
  return decorator

# 这个3层嵌套的decorator用法如下：
@log('execute')
def now():
  print('2018-11-23')

# 执行结果如下：
now() # execute now(): 2018-11-23

# 和2层嵌套的decorator相比，3层嵌套的效果是这样的： now = log(‘execute’)(now)

# 我们来剖析上面的语句，首先执行 log(‘‘execute’)，返回的是decorator函数，
# 在调用返回的函数，参数是now函数，返回值最终是wrapper函数。

# 意思两种decorator的定义都没有问题，但还差最后一步。
# 因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，他们的__name__已经从原来的’now‘变成了’wrapper‘：
now.__name__   # 'wrapper'

# 因为返回的那个wrapper()函数名字就是’wrapper‘，
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会报错

# 不需要编写 wrapper.__name__ = func.__name__这样的代码,python内置的functions.wraps就是干这个事的，
# 所以一个完整的decorator的写法如下：
import functools
def log(func):
  @functools.wraps(func)
  def wrapper(*args,**kw):
    print('call %s():' % func.__name__)
    return func(*args,**kw)
  return wrapper


# 或者针对带参数的decorator
import functools
def log(text):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
      print('%s %s():' % (text,func.__name__))
      return func(*args,**kw)
    return wrapper
  return decorator


# import functools 是导入functools模块。

@log('execute')
def now():
  print('2018-11-23')

now.__name__   # 'now'














# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time,functools
def metric(fn):
  print('%s executed in %s ms' %(fn.__name__,10.24))
  return fn

# 测试
@metric
def fast(x,y):
  time.sleep(0.0012)
  return x+y

@metric
def slow(x,y,z):
  time.sleep(0.1234)
  return x * y * z

f = fast(11,22)
s = slow(11,22,33)
if f != 33:
  print('测试失败')
elif s != 7986:
  print('测试失败')



# 我的答案
def myMetric(func):
  @functools.wraps(func)
  def wrapper(*args,**kw):
    begin = time.time()
    func(*args,**kw)
    end = time.time()
    print("%s executed in %s ms" %(func.__name__,end-begin))
    return func(*args,**kw)
  return wrapper
































































