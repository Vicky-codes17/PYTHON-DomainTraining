### Write a program to display the flames of two names

a = input("Enter the boy name : ")
b = input("Enter the girl name : ")

a1 = list(a)
b1 = list(b)

for i in range(len(a1)):
    for j in range(len(b1)):
        if a1[i] == b1[j]:
            a1[i] = '0' 
            b1[j] = '0' 
            break
print(f"Name 1: {a1}")
print(f"Name 2: {b1}")

c = 0
for i in a1:
    if i != '0':
        c = c + 1

for i in b1:
    if i != '0':
        c = c + 1

print(f"Total remaining characters: {c}")

f = 0
res = list("FLAMES")
while len(res) != 1:
    f = (f + (c - 1)) % len(res)
    d = res.pop(f)
    print(f"Removed: {d}, Remaining: {res}")

flames_meaning = {
    'F': 'Friends',
    'L': 'Love',
    'A': 'Affection', 
    'M': 'Marriage',
    'E': 'Enemy',
    'S': 'Sister'
}

result = res[0]
print(f"\nResult: {result} - {flames_meaning[result]}")
