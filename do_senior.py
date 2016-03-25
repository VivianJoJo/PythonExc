L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前3个元素
L[0:3]
L[:3]

#倒数切片
 L[-2:]
  L[-2:-1]


L = list(range(100))
#前10个数，每两个取一个
L[:10:2]

#每5个取一个
L[::5]

#tuple也可以用切片操作，只是操作的结果仍是tuple
(0, 1, 2, 3, 4, 5)[:3]
#字符串也可以用切片操作，只是操作结果仍是字符串
'ABCDEFG'[::2]

--------
#迭代
#生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(1, 11))
#生成[1x1, 2x2, 3x3, ..., 10x10]
#way1:
>>> L = []
>>> for x in range(1, 11):
...    L.append(x * x)
...
>>> L
#way2
[x * x for x in range(1, 11)]


#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]

#使用两层循环，可以生成全排列：
>>> [m + n for m in 'ABC' for n in 'XYZ']







--------
--------------
#列表生成式的[]改成()，就创建了一个generator：
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>


#打印
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print(n)
... 


------------
#迭代器
#可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

 from collections import Iterable
 isinstance([], Iterable)
 isinstance({}, Iterable)
 isinstance((x for x in range(10)), Iterable)
 isinstance(100, Iterable)


 ---------
 #高阶函数   
 def add(x, y, f):
    return f(x) + f(y)

add(-5, 6, abs)


-------
