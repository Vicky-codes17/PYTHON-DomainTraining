### Write a Python program to demonstrate the use of the append() method.

a = []
for i in range(1,100):
    if(i%5 == 0):
        a.append(a)
print(i)