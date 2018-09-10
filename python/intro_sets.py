def average(arr):

    set1 = (set(arr))
    set2 = sum(set1)
    length = len(set1)
    avg = set2/length
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


