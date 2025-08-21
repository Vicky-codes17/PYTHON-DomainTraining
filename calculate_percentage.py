### Write a Python program to calculate the percentage of marks obtained by students.

student = ["Ram","Vignesh","Vicky","Viki"]
marks = [[20,26,12,33],[33,45,33,26],[33,23,12,32],[34,12,34,22]]
per = []
for i in marks:
    d = sum(i) // 3
    per.append(d)

for i in range(4):
    print("{}.{} : {}".format(i+1,student[i],per[i]))