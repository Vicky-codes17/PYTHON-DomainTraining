### Print a list which contains 5 randomly generating number(1 to 10) without dulipcation

import random

l1 = []
while (len(l1)  != 5):
    rand = random.randint(1,10)
    if (rand not in l1):
        l1.append(rand)
print(l1)