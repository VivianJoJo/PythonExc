#字符串 示例#
#字符串是以单引号'或双引号"括起来的任意文本
#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('I\'m ok.')
print('\\\n\\')

#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
>>> print('''line1s = 
... line2
... line3''')

#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
ord('A')  
ord('中')
chr(66)
chr(25991)

#要计算str包含多少个字符，可以用len()函数
len('ABC')
len('中文')
len('中文'.encode('utf-8'))


#布尔值
>>> True
True
>>> False
False
>>> 3 > 2
True
>>> 3 > 5
False

#布尔值可以用and、or和not运算
>>> True and True
True
>>> True and False
False

>>> True or True
True
>>> True or False
True

>>> not True
False
>>> not False
True
>>> not 1 > 2
True

#这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
#静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

a = 'ABC'
#Python解释器干了两件事情：
#在内存中创建了一个'ABC'的字符串；
#在内存中创建了一个名为a的变量，并把它指向'ABC'。
#也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：

a = 'ABC'
b = a
a = 'XYZ'
print(b)
a = 'XYZ'
print(b)