
def mergeSort(a):
    if len(a)>1:
        mid = len(a)//2
        a1 = a[:mid]
        a2 = a[mid:]
        return merge(mergeSort(a1),mergeSort(a2))
    else:
        return a

def merge(a,b):
    l1,l2 = len(a),len(b)
    a.append(99999999999)
    b.append(99999999999)
    A = []
    i = j = k = 0
    while i < l1+l2:
        if a[j] <= b[k]:
            A.append(a[j])
            j+=1
        else:
            A.append(b[k])
            k+=1
        i+=1
    return A

import time
import random
import math
from matplotlib import pyplot as pp

x,y = [],[]
for i in range(1,11):
    a = []
    size = i*10000
    x += [size]

    a = [random.randint(1,size) for _ in range(size)]

    t1 = time.time()
    mergeSort(a)
    t2 = time.time()

    y += [t2-t1]
    print(t2-t1)


pp.plot(x, y, color = 'y', label="nlogn")
pp.scatter(x, y, color = 'g')
pp.show()
