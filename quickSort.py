from random import randint

def qsort(arr,left,right):
    print("sorting",arr[left:right+1])
    if left == right:
        return arr
    else:
        pivot = partition(arr,left,right)
        qsort(arr,left,pivot-1)
        qsort(arr,pivot+1,right)

            
def partition(arr,left,right):
    pivot = randint(left,right)
    item = arr[pivot]
    print("pivot element",item)
    while left < right:
        while arr[left] <= item :
            left += 1
        while arr[right] > item :
            right -= 1
        if arr[left] > item and arr[right]<item:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        print("struct",left,right)
    return left
    
arr = [5,9,8,7,6,3,1,4,2,6]
qsort(arr,0,len(arr)-1)
print(arr)
