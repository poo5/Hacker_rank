import random
from datetime import datetime
if __name__ == '__main__':

    n = int(input())
    arr1 = map(int, input().split())
    start = datetime.now()
    arr = sorted(arr1)
    while arr[-2] == arr[-1]:
        arr.remove(arr[-1])
    print(arr[-2])
    end = datetime.now() - start
    print(end)

