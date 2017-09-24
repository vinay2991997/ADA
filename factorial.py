def fact(n):
    ans = 1
    for i in range(n):
        ans *= i+1
    return ans

a = int(input())
print(fact(a))
