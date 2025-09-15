### 8) Hollow Rectangle Pattern
r = 5
c = 5
for i in range(r):
    for j in range(c):
        if i == 0 or i == r - 1 or j == 0 or j == c - 1:
            print("A", end=" ")
        else:
            print(" ", end=" ")
    print()