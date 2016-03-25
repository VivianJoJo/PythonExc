classmates = ['Michael', 'Bob', 'Tracy']
classmates

#list元素的个数
len(classmates)

#用索引来访问list中每一个位置的元素，记得索引是从0开始的
classmates[0]

#取最后一个元素
classmates[-1]
#倒数第2个
classmates[-2]

#追加元素到末尾
classmates.append('Adam')

#把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'Jack')

#删除list末尾的元素
classmates.pop()

#list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]

#list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
len(s)

#空的list
L = []
len(L)   0

------------------------
#空的tuple
t = ()

#只有1个元素的tuple
 t = (1,)

 #“可变的”tuple
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])

------------
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