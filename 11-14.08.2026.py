#set assingment

#create a set of  fruts consisnting of name of 10fruits . create another set of summer fruits that consist s of fruits that re available only in summer season . 
#create another set wintr fruit consisntg of 5 fruits of winter season .
#now perform the following opns on the sets 
#1. print thte name of all fruits in 3sets 
#2. print the name of fruits thare present in fruits and winter fruit 
#3. print fruits name that re present only in summer fruit set but not in  fruits set
#4. print the  name of fruits that are present in summer fruit set and winter fruit set but not in fruits set
#5. find whether orange is present in  fruit set or not
#6. find in which set pineapple is present
 

fruits = {
    "Apple", "Mango", "Orange", "Banana", "Pineapple",
    "Grapes", "Watermelon", "Guava", "Papaya", "Strawberry"
}

summer_fruits = {
    "Mango", "Watermelon", "Papaya", "Litchi", "Muskmelon"
}

winter_fruits = {
    "Apple", "Orange", "Strawberry", "Guava", "Kiwi"
}


# 1
print("1. Fruits Set:", fruits | summer_fruits | winter_fruits)



# 2
print("\n2. Fruits present in Fruits and Winter Fruits:")
print(fruits & winter_fruits)


# 3
print("\n3. Fruits present only in Summer Fruits but not in Fruits:")
print(summer_fruits - fruits)


# 4
print("4. Fruits present in Summer and Winter but not in Fruits:")
print((summer_fruits & winter_fruits) - fruits)


# 5
print("5. Is Orange present in Fruits set?")

if "Orange" in fruits:
    print("Yes, Orange is present.")
else:
    print("No, Orange is not present.")


# 6
print("6. Pineapple is present in:")

if "Pineapple" in fruits:
    print("Fruits set")

if "Pineapple" in summer_fruits:
    print("Summer Fruits set")

if "Pineapple" in winter_fruits:
    print("Winter Fruits set")