import random

#Creation of empty list
random_list = []
#Addition of 100 values to the list that are in range from 100 to 999
for i in range(100):
    random_list.append(random.randint(100, 999))
#Finding the maximum,minimum and average of all values in the list
max_value = max(random_list)
min_value = min(random_list)
average_value = sum(random_list) / len(random_list)
#Printing the maximum, minimum and average values
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
print(f"Average: {average_value}")