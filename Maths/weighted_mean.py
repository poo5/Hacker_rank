import pandas as pd
import numpy as np
n = int(input())
arr = list(map(int, input().rstrip().split()))
arr1 = list(map(int, input().rstrip().split()))

for i in range(n):
    arr[i] = arr[i]*arr1[i] /sum(arr1)
rate = sum(arr)
print(round(rate,1))


