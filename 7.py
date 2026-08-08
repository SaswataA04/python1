#wpp to define a  ethod  checkArmstrong(num) to check whether num is armstrong or not , IF yes return true else return false    

def checkArmstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** digits
        num //= 10

    return total == original


n = 153

if checkArmstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")