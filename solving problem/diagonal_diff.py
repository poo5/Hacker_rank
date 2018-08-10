import numpy as np
def diag(arr):
    l = 0
    r = 0
    l = sum(arr[i][i] for i in range(n))
    r = sum(arr[i][n-i-1] for i in range(n))
    return(abs(l-r))

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    print(diag(arr))


