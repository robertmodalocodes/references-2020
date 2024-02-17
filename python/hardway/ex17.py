from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file).read()

print(f"The input file is {len(in_file)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_file)

print("Alright, all done.")
print("--"*20)

out_file.close()
# in_file.close()

# open the text and see if it is already written
with open('new_file.txt', 'r') as smokeread:
    print(smokeread.read())
    smokeread.close()
