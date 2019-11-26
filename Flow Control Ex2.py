def max_of_three() :
    x = float(input("Please input x value: "))
    y = float(input("Please input y value: "))
    z = float(input("Please input z value: "))
    if x > y and z :
        print("x is larger")
    elif y > x and z :
        print("y is larger")
    elif z > y and x :
        print("z is larger")
    else:
        print("They are equal")
max_of_three()