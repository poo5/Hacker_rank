'''Works only for small set of inputs'''


'''def shift_list(l,n):


    return l[-n % len(l):] + l[:-n % len(l)]



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = shift_list(a,n)
    print(result)'''



# Python implementation of left rotation of
# an array K number of times

# Function to leftRotate array multiple times
'''def shift_list(arr, n, k):

    # To get the starting point of rotated array
    mod = k % n
    s = ""

    # Prints the rotated array from start position
    for i in range(n):
        a = str(arr[(mod + i) % n])
        print(a,end=' ')

# Driver program
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    shift_list(a,n,d)'''

a = 'A'
print(a)
