def plusMinus(arr):
    pos = 0
    neg = 0
    zero_count = 0
    for i in arr:
        if i > 0:
            pos = pos+ 1
        elif i < 0:
            neg = neg + 1
        else:
            zero_count = zero_count + 1

    pos_cal = pos/n
    neg_cal = neg/n
    zero_cal = zero_count/n
    return(pos_cal,neg_cal,zero_cal)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print("%.6f\n%.6f\n%.6f\n" %plusMinus(arr))



