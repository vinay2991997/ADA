def fib(n):
    first = 1
    second = 1
    for i in range(n-2):
        first,second = first+second,first
    return first

n = int(input())
print(fib(n))
