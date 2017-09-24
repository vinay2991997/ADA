
from time import time
from random import randint

def assign(n,size):
    c = []
    for i in range(size):
        x = []
        for j in range(size):
            x.append(int(n))
        c.append(x)
    return c

def assign1(size):
    c = []
    for i in range(size):
        x = []
        for j in range(size):
            x.append(int(randint(1,100)))
        c.append(x)
    return c

def smul(a,b):

    if len(a) != 2 :
        return
    
    c = assign(0,len(a))
    
    p1 = (a[0][0]+a[1][1])*(b[0][0]+b[1][1])
    p2 = (a[1][0]+a[1][1])*(b[0][0])
    p3 = (a[0][0])*(b[0][1]-b[1][1])
    p4 = (a[1][1])*(b[1][0]-b[0][0])
    p5 = (a[0][0]+a[0][1])*(b[1][1])
    p6 = (a[1][0]-a[0][0])*(b[0][0]+b[0][1])
    p7 = (a[0][1]-a[1][1])*(b[1][0]+b[1][1])

    c[0][0] = p1+p4-p5+p7
    c[0][1] = p3+p5
    c[1][0] = p2+p4
    c[1][1] = p1+p3-p2+p6

    return c


#a = assign(1,2)
#a = [[1,2],[3,4]]

a = assign1(2)
b = assign1(2)

print(a,b)

t1 = time()
c = smul(a,b)
t2 = time()

print(c)
print("Time taken is",t2-t1)
