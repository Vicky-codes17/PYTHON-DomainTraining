### 5) Take User Numbers,Add them to sum and if user enter 0 .Print the total

sum = 0
n = 1
while n != 0:
    n = int(input("Enter a number (0 to stop): "))
    if n < 0 or n > 100:
        continue
    sum = sum + n
print("Sum of user inputs is:", sum)