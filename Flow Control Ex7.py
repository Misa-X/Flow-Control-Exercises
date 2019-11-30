
string = input("Please enter string: ").lower()
string1 = string.replace(" ", "")

reversed_string = string1[::-1]
print("reversed_string: ", reversed_string)
def is_palindrome() :
    if string1 == reversed_string:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")

is_palindrome()