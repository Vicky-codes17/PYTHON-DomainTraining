a = "123"

sum = 0
for i in a:
      x = ord(i) - ord('0')
      sum = sum*10 + x
print(sum)              # 123
