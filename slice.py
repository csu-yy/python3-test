# -*- coding: UTF-8 -*-

# 通常一个切片操作要提供三个参数 [start_index:  stop_index:  step]  
# start_index是切片的起始位置
# stop_index是切片的结束位置（不包括）
# step可以不提供，默认值是1，步长值不能为0，不然会报错ValueError。

# 取一个list或者tuple的部分元素  
L = ['Michael','Sarah','Tracy','Bob','Jack']
# 取 L的 前三个元素
# 法一  笨方法： L[0] L[1] l[2]

# 取前N个元素，也就是索引为0-(N-1)的元素，可以用循环
# 取 L 的前三个元素
def test(n):
  r = []
  for i in range(n):
    r.append(L[i])
  return r
print(test(3))

# 利用python提供的切片（Slice）操作符，大大简化操作
# 用切片取 L 的前三个元素
print(L[0:3])  # ['Michael', 'Sarah', 'Tracy']


#  切片  相关解释
L[0:3]  # 表示，从索引0开始取，直到索引3为止，但不包括索引3.即索引0、1、2，正好是3个元素。如果第一个索引是0，还可以省略‘:’  即L[:3]
print(L[1:3])  # ['Sarah', 'Tracy']

# python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
L[-2:]  # 【'Bob','Jack']
L[-2:-1]  # ['Bob']

# 记住： 倒数第一个元素的索引是-1
# 切片操作十分有用  
LL = list(range(100)) # 创建一个0-99的数列  [0,1,2,3,...,99]
#通过数列轻松取出一段数列
ll = LL[:10]   # 前10个      [0,1,2,3,4,5,6,7,8,9]
ll = LL[-10:]  # 后10个      [90,91,92,93,...,99]
ll = LL[10:20] # 前11-20个   [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

ll = LL[:10:2]  # 前10个数，每2个取一个  [0,2,4,6,8]
ll = LL[::5]    # 所有数，每5个取一个    [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# 什么都不写，只写：就可以原样复制一个list
ll = LL[:]    # [0,1,2,3,...,99]

# tuple 也是一种list 唯一区别是tuple不可变，因此，tuple也可以用切片操作，只是操作的结果仍是tuple
(0,1,2,3,4,5)[:3]  # (0,1,2)

# 字符串 ‘XXX’ 也可以看成是一种list，每个元素就是一个字符。因此字符串也可以用切片操作，操作的结果仍是字符串
'ABCDEFG'[:3] # 'ABC'










# 练习
# 利用 ‘切片’ 实现 字符串的strip功能（去掉字符串的首位空格）
def trim(s):
  if not isinstance(s, (str)) :
    raise TypeError("arg error")
  if s == '':
    return s
  # 左判断
  while 0<len(s) and ' ' == s[0:1] :
    s = s[1:]
  # 右判断
  while 0<len(s) and ' ' == s[-1] :
    s = s[0:-1]
  return s


# 测试
def main():
  if trim('hello  ') != 'hello':
      print('测试失败!')
  elif trim('  hello') != 'hello':
      print('测试失败!')
  elif trim('  hello  ') != 'hello':
      print('测试失败!')
  elif trim('  hello  world  ') != 'hello  world':
      print('测试失败!')
  elif trim('') != '':
      print('测试失败!')
  elif trim('    ') != '':
      print('测试失败!')
  else:
      print('测试成功!')

main()