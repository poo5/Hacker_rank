def catAndMouse(x, y, z):
    s = ""
    if abs(z-y) < abs(z-x):
        return("Cat B")
    elif abs(z-y) == abs(z-x):
        return("Mouse C")
    elif abs(z-y) > abs(z-x):
         return("Cat A")



if __name__ == '__main__':

    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        print(result)

