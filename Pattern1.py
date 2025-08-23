### 3) Left Triangle
### Printing a pattern using nested loops using *
p = 5
for i in range(p):
    for j in range(i + 1):
        print("*", end="")
    print()