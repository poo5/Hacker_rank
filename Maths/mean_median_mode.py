from scipy import stats
import numpy as np
n = int(input())
arr = list(map(int, input().rstrip().split()))
a = sorted(arr)
sum = 0
for i in a:
    sum +=i
print(sum/n)
 #print(np.mean(arr)) print mean
length = int(len(a)/2)
x4 = a[length-1]
x5 = a[length]
median = (x4+x5)
print(median/2) #calulating median
#print(np.median(arr)) //also prints median
#ptint(statistics.median(arr)) importing statistics and printing fetchs same

print(int(stats.mode(arr)[0]))


'''dict ={}

arr = [4978, 11735,14216,4978]
for i in range(4):
    dict[i] = arr[i]

for k,v in dict.items():
    if v in dict:
        p


for i in range(3):
    dict[i] = arr[i]

for k,v in dict.items():
    if v in dict:'''
        


