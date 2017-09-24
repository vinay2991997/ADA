#min max using divide and conquer
from random import randint

class pair:
    def __init__(self,mi,ma):
        self.mi = min(mi,ma)
        self.ma = max(mi,ma)
    def __repr__(self):
        return "("+str(self.mi)+","+str(self.ma)+")"
    def __str__(self):
        return "Min : " + str(self.mi) + "\nMax : " + str(self.ma) 


def func(arr):
    if len(arr) == 1:
        return pair(arr[0],arr[0])
    elif len(arr) == 2 :
        return pair(min(arr),max(arr))
    else:
        mid = len(arr)//2
        a = func(arr[:mid])
        b = func(arr[mid:])
        return pair(min(a.mi,b.mi),max(a.ma,b.ma))


arr = [randint(1,100) for i in range(10)]
print(arr)

print(func(arr))
