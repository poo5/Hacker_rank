def cmp(a,b):

    index1 = 0
    index2 = 0
    for i in range(3):

        if a[i] > b[i]:
            index1= index1+1
        elif a[i] < b[i]:
            index2= index2+1
    return (index1,index2)

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = cmp(a,b)
    print(' '.join(map(str,result)))
    print('\n')
