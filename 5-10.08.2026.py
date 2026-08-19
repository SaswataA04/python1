


# WPP to define a method isPrime(num) to check whether a number is prime or not

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if isPrime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")