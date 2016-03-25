#比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：

import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny


# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)


# r = move(100, 100, 60, math.pi / 6)
# print(r)



#高阶函数 
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))