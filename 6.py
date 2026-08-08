#wpp to define a method doSUm(num) to find the sum of all nos OF  num and return the result

def doSum(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    return total


n = 12345
print("Sum of digits =", doSum(n))