### Write a program printing the students marks based on the rank

students = [
    {"name":"Vignesh","dept":"cse","marks":[20,40,55]},
    {"name":"Viki","dept":"cse","marks":[40,45,65]},
    {"name":"Vignesh R","dept":"cse","marks":[80,70,75]},
    {"name":"Ram","dept":"cse","marks":[60,65,70]}
]

for i in students:
    total = sum(i["marks"])
    d = total//3
    i["per"] = d

res = sorted(students,key=lambda x:x["per"],reverse= True)

des = ["FIRST","SECOND","THIRD","FOURTH"]

for i in range(4):
    print("RANK {}.{} {} has scored {}".format(i+1,res[i]["name"],res[i]["per"],des[i]))