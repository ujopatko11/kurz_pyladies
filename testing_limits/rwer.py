
"""
x=[1,2,3,4,5,6]
print(tuple(x[3:4]))


print(list(range(0,10,2)))
print([i * 2 for i in range(5)])
print(list(reversed(range(8,-1,-2))))
print([i for i in range(10) if i % 2])
print(0xA + 0xa)

class X:
    def __init__(self, a):
        self.a = a
        a = 2

x = X(1)
print(x.a)"""


def solution(A, B):
    cnt = 0
    for i in range(A, B + 1):
        j = 1;
        while j ** 2 <= i:
            if j ** 2 == i:
                cnt += 1
            j += 1
        i += 1
    return cnt
print(solution(4,17))