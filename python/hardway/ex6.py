# set set of people variable to 10
types_of_people = 10
# a string is put inside a string and set it to a variable 1
x = f"There are {types_of_people} types of people"

# other string variables
binary = "binary"
do_not = "don't"
# the string are put inside a string which is set to another variable 2 and 3
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# a string inside a string 4
print(f"I said: {x}")
# a string inside a string 5
print(f"I also said: '{y}'")

hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

# boolean is placed inside a string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
# the strings are added onto each other
