def gradingStudents(grades):
    result = []
    for i in grades:
       if i< 38:
           result.append(i)
       else:
           a = i%5
           if a<3:
               result.append(i)
           else:
               i = (i-a)+5
               result.append(i)
    return result


if __name__ == '__main__':
    n = int(input())
    grades = []
    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
