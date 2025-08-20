### Case Conversions Method 1
a  = "123"
b = [int(i) for i in a]

sum = 0
for i in range(3):  # for i in b:
  sum = sum*10 + 1
print(sum)          # 123

### Case Conversions Method 2

a = "123"

sum = 0
for i in a:
      x = ord(i) - ord('0')
      sum = sum*10 + x
print(sum)              # 123

    
