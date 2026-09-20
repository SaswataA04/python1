#Consider a scenario where 2 cars are moving from a point p and another from point q in the same direction and meet each other after 11 hours. 
# If they move in the opposite direction they will meet after 1 hour. 
#find the velocity of both cars


# Time taken when cars move in the same direction
same_direction_time = 11

# Time taken when cars move in opposite directions
opposite_direction_time = 1

# Let speed of car 1 = v1
# Let speed of car 2 = v2

# From:
# v1 - v2 = D / 11
# v1 + v2 = D / 1

# Therefore:
# v1 + v2 = 11(v1 - v2)

# Solving:
# 10v1 = 12v2
# v1 / v2 = 6 / 5

print("Ratio of velocities of the two cars = 6 : 5")

# If distance between P and Q is known
distance = float(input("Enter distance between P and Q in km: "))

# Opposite direction:
# v1 + v2 = distance

# Ratio = 6 : 5
v1 = distance * 6 / 11
v2 = distance * 5 / 11

print("Velocity of Car 1 =", v1, "km/h")
print("Velocity of Car 2 =", v2, "km/h")