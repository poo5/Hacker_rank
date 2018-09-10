a = [1,2,4,5,3]
n = 5
i = n-1
temp = a[i]
while a[i-1] >temp and i>0:
    a[i]=a[i-1]
    print(' '.join(map(str,a)))
    i-=1
a[i]=temp
print(' '.join(map(str,a)))







    

