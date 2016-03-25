d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95

#way1:通过in判断key是否存在
>>> 'Thomas' in d

#way2:dict提供的get方法,如果key不存在，可以返回None，或者自己指定的value   返回None的时候Python的交互式命令行不显示结果。
>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1

#删除一个key，用pop(key)方法
d.pop('Bob')


#和list比较，dict有以下几个特点：

#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。
#而list相反：

#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。


#创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
s = set([1, 1, 2, 2, 3, 3])

#add(key)方法可以添加元素到set
s.add(4)

#remove(key)方法可以删除元素
 s.remove(4)

 #两个set可以做数学意义上的交集、并集等操作
 >>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}


#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
>>> a = ['c', 'b', 'a']
>>> a.sort()
>>> a
['a', 'b', 'c']


#而对于不可变对象
>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc'
