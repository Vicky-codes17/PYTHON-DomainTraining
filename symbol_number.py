r = 6
c = 6
for i in range(r):
    for j in range(c):
        if i == 0 or i == r - 1 or j == 0 or j == c - 1:
            print("A", end=" ")
        elif i == 1 or i == r - 1:
            print("*",end = " ")
        elif i == 2 or i == r - 1:
            print("$",end = " ")
        elif i == 3 or i == r - 1:
            print("*",end = " ")
        elif i == 4 or i == r - 1:
            print("$",end = " ")
        elif i == 5 or i == r - 1:
            print("*",end = " ")
    
        else:
            print(" ", end=" ")
    print()