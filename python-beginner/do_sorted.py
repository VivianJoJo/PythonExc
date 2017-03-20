from operator import itemgetter

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#按名字排序
def bt_name(t):
	return t[0]
L2 = sorted(students, key=bt_name)
print(L2)

# print(bt_name(('Bob', 75)))

#按分数排序
def by_score(t):
    return t[1]
L3 = sorted(students, key=by_score, reverse=True)
print(L3)

# print(by_score(('Bob', 75)))


# print(itemgetter(0))
# print(sorted(students, key=itemgetter(0)))


#匿名函数   计算f(x)=x2
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

#也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y