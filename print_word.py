### 2) Printing "hai" 5 times with loop and also print counter

c = 2
for i in range(3):          # i = 0,1,2
    for j in range(5):      # j = 0,1,2,3,4
        print("hai",end=" ")
        c = c + 2
    print(c,end=" ")
    print()