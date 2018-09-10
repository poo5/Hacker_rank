import statistics
'''n1 = int(input())
a = list(map(int, input().rstrip().split()))'''

a = [3,7,8,5,12,14,21,13,18]
sorted_list = sorted(a)

n= n1/2


if n%2 ==0:
    n = int(n)
    L = sorted_list[:n-1]
    U = sorted_list[n+1:]
    q1 = statistics.median(L)
    q2 = statistics.median(sorted_list)
    q3 = statistics.median(U)
    print(int(q1))
    print(int(q2))
    print(int(q3))


else:
    n = int(n)
    L = sorted_list[:n]
    U = sorted_list[n+1:]
    q1 = statistics.median(L)
    q2 = statistics.median(sorted_list)
    q3 = statistics.median(U)
    print(int(q1))
    print(int(q2))
    print(int(q3))

