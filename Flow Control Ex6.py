string = input("Please enter string: ")
reversed_string = string[::-1]
print("reversed_string: ", reversed_string)
def is_palindrome() :
    if string == reversed_string :
        print("String is a palindrome")
    else:
        print("String is not a palindrome")

is_palindrome()
