
from time import time
from random import randint

def minmax(arr):
    mi = ma = arr[0]
    for i in arr:
        if mi > i:
            mi = i
        if ma < i:
            ma = i
    return mi,ma

size = 100
arr = [randint(1,100) for i in range(size)]
print(arr)
mi,ma = minmax(arr)
print('Min :',mi,'Max :',ma)
