text = 'D:/Programming/Python2/Hardway/test.txt'

with open(text) as test:
    print(test.read())
    test.close()


read_text = open(text, 'r')
print(read_text.read())
read_text.close()
