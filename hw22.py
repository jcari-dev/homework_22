# Exercises
# Exercise 1
# Create a list named students containing some student names (strings).


students = ['Jorge', 'Maria', 'Chris', 'Peiyi',
            'Asher', 'Handsome', 'Michael', 'Rafael', 'Hayley']


# Print out the second student's name.


print(students[1])


# Print out the last student's name.


print(students[-2])


# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.


foods = ('Pizza', 'IceCream', 'Spaghetti', 'Hotdogs',
         'French Fries', 'Chicken', 'Sushi', 'Pad Thai', 'Pho')


# Use a for loop to print out the string "food goes here is a good food".


for x in foods:
    print('food goes here is a good food')


# Exercise 3
# Using a for loop, print just the last two food strings from foods.


y = 0
for a in foods:
    y += 1
    if y == len(foods) - 1 or y == len(foods):
        print(a)


# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.


home_town = {
    'city': 'Santo Domingo',
    'state': 'Distrito Nacional',
    'population': '3,000,000'
}

# Print a string with this format:
# "I was born in city, state - population of population"


print(
    f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"

for key, val in home_town.items():
    print(f"{key} = {val}")

# Exercise 6
# Create an empty list named cohort.


cohort = []


# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:

#  {
#  	'student': 'Tina',
#  	'fav_food' 'Cheeseburger'
#  }

n = 0
for r in students:
    a = {'student': r, 'fav_food': foods[n]}
    n += 1
    cohort.append(a)

print(cohort)


# Iterate over cohort printing out each element.

for q in cohort:
    print(q)

# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]

awesome_students = []

for w in students:
    awesome_students.append(f'{w} is awesome!')


# Iterate over awesome_students printing out each string.


print(awesome_students)


# Exercise 8
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.


for k in foods:
    if 'a' in k:
        print(k)
    else:
        print("'a' not found")
