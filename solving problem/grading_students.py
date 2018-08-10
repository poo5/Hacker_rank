i = [73,67,38,33]
for a in i:
    if a >37 and a%5!=0:
        p = a%5
        q = (a-p)+5
        print(q)
    else:
        print(a)

