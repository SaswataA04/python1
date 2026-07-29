# wpp to take a year and see if its leap yr or not

year = int(input("enter the year"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print("leap yr")

else:
    print("not leap yr")  