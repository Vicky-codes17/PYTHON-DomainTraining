### Create a list of numbers from user input until the list has 5 unique elements.
l1 = []

while(len(l1) !=5):
    a = int(input("Enter any number : "))
    if a in l1:
        print("This number already exist")
    else:
        l1.append(a)
print(l1)