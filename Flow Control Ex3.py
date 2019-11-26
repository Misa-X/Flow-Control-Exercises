def string_length():
    count = 0
    for i in string:
        count = count+1
    return count

string = input("Please enter string: ")
print("String length is: ", string_length())
