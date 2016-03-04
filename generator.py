#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### text 
s = (x * x for x in range(5))
print(s)

for x in s:
	print(x)

###  斐波那契
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	# return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
	print(x)

g = fib(5)
while 1:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e)
		break

### 杨辉三角
def triangles():
	l = [1]
	yield l
	while True:
		l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
		yield l

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
