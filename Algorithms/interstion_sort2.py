arr=[1,4,3,5,6,2]
n = 6
i = 1
for i in range(n-1):
    j = i
    value = arr[i]
    while j>=1 and arr[j-1]>value:
        arr[j]=arr[j-1]
        j -=1
    arr[j] = value
    print(' '.join(map(str,arr)))


