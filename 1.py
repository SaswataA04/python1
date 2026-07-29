# wpp to create a calculator that takes 2 nos from user and performs basic arithmetic operations like addition, subtraction, multiplication, and division.

a = int(input("enter first no"))
b = int(input("enter second no"))
choice = int(input("enter choice"))

match choice:
    case 1:
        result = a+b
    case 2:
        result = a-b
    case 3:
        result = a*b
    case 4:
        result = a/b
    case _:
        result = "unknown"

print(result)