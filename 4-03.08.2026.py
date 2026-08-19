

    # WPP to define a method factorial that takes a parameter
# and returns the factorial of the number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))