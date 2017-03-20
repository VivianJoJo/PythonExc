#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#### 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
#### 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

# def normalize(name):
# 	return name[0].upper() + name[1:].lower()

# L1 = ['adam', 'LiTS', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)



# #### 编写一个prod()函数，可以接受一个list并利用reduce()求积
# from functools import reduce
# def prod(L):
# 	def f(x, y):
# 		return x * y
# 	return reduce(f, L)

# print('1 * 2 * 3 * 4 =', prod([1, 2, 3, 4]))


#把str '12345'转换为int
from functools import reduce
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print('\'12452\' ->  ', str2int('12452'))

#### 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# from functools import reduce
# def str2float(s):
# 	def fn(x, y):
# 		return x * 10 + y
# 	def char2num(s):
#     	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	
# 	L = list(s)
# 	i = 0
# 	while L[i] != '.':
# 		i = i + 1
# 	num1 = reduce(fn, map(char2num, L[:i]))
# 	num2 = reduce(fn, map(char2num, L[i+1:]))/pow(10, len(L[i+1:]))
# 	return num2 + num1

# print('str2float(\'123.456\') =', str2float('123.456'))