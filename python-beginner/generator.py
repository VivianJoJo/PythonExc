#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### text 
# s = (x * x for x in range(5))
# print(s)

# for x in s:
# 	print(x)

#原斐波那契
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# print(fib(6))


###  斐波那契
# print("----------")

def fib_g(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

# print(fib_g(6))

# f = fib_g(10)
# print('fib——g(10):', f)
# for x in f:
# 	print(x)


# g = fib_g(10)
# while 1:
# 	try:
# 		x = next(g)
# 		print('g:', x)
# 	except StopIteration as e:
# 		print('Generator return value:', e)
# 		break


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)
next(o)

# next(o)



#迭代器

# from collections import Iterable
# isinstance([], Iterable)
# isinstance({}, Iterable)
# isinstance((x for x in range(10)), Iterable)
# isinstance(100, Iterable)

### 杨辉三角
# def triangles():
# 	l = [1]
# 	yield l
# 	while True:
# 		l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
# 		yield l

# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break
