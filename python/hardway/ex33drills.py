# ex33 drills
# 1
i = 0
numbers = []

def print_loop(rand, increment):
	'''Adds a value to a list and prints the list'''
	global i, numbers
	while i < rand:
		print(f"At the top i is {i}")
		numbers.append(i)

		i = i + increment
		print("numbers now: ", numbers)
		print(f"At the bottom i is {i}")


print_loop(int(input("enter a range\n> ")), int(input("enter an increment\n> ")))
print("")

print("The numbers")

for num in numbers:
	print(num)

print("")

# 5
# convert to a for loop
numbers2 = []
rand = int(input("Enter a range:\n> "))
increment = int(input("Enter an increment:\n> "))

for i in range(0, rand, increment):
	print(f"At the top i is {i}")
	numbers2.append(i)

	# i = i + increment
	print("numbers now: ", numbers2)
	print(f"At the bottom i is {i}")

print("")

for num in numbers2:
	print(num)
