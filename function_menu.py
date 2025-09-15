def sq():
    side = int(input("Enter the side of the square: "))
    area = side * side
    print("Area of square is:", area)
def rect():
    l = int(input("Enter the lenght  :"))
    b = int(input("Enter the breadth : "))
    area = l * b
    print("Area of Rectangle is:", area)
def circle():
    r = int(input("Enter the radius of the circle: "))
    res = 3.14 * r * r
    print("Area of Circle is:", res)
def tri():
    b = int(input("Enter the base of the triangle: "))
    h = int(input("Enter the height of the triangle: "))
    x = 0.5 * b * h
    print("Area of Triangle is:", x)

while(1):
    print("1.Square")
    print("2.Rectangle")
    print("3.Circle")
    print("4.Triangle")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sq()
    elif choice == 2:
        rect()
    elif choice == 3:
        circle()
    elif choice == 4:
        tri()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
