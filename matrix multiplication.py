
from time import time

def assign(n,size):
    c = []
    for i in range(size):
        x = []
        for j in range(size):
            x.append(int(n))
        c.append(x)
    return c

def mul(a,b):
    #c = [[0]*len(a)]*len(a)
    c = assign(0,len(a))

    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                c[i][j] += a[i][k]*b[k][j]
    return c


a = assign(1,100)
t1 = time()
c = mul(a,a)
t2 = time()
print(c)
print("Time taken is",t2-t1)
