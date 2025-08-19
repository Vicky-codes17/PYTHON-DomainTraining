### LCM of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

big = max(a, b)
step = big

while True:
    if big % a == 0 and big % b == 0:
        print(f"LCM of {a}, and {b} is:", big)
        break
    else:
        big += step