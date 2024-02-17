name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = height * 2.54
weight_kg = weight / 2.205

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffe.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print("")
print("Oh wait I converted the weight and height into kg and cm.")
print(f"His weight is {round(weight_kg, 2)} in kilograms.")
print(f"And his height is {round(height_cm, 2)} in centimeters.")
