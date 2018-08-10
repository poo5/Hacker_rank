if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        avgdict = {}
        for k,v in student_marks.items():
            avgdict[k] = sum(v)/len(v)
    query_name = input()
    print("%.2f" % avgdict[query_name])
