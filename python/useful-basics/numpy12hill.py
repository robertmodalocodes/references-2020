import numpy as np

DATABASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']

key = np.array([10, 15, 20, 25])  # key order

# converting the alphabets into integers


def alpha_to_int(alpha):
    num = np.zeros(len(alpha))
    for i in range(0, len(alpha)):
        for j in range(0, len(DATABASE)):
            if alpha[i] == DATABASE[j]:
                num[i] = j
                break
    return num

# converting the integers into alphabets


def int_to_alpha(num):
    alpha = ''
    for i in range(0, len(num)):
        num = num + DATABASE[int(num[i])]
    return alpha


def encrypt(plain, key):
    num = alpha_to_int(plain)  # change
    num2 = np.zeros(len(num))  # container variable
    j = 0
    for i in range(0, len(num)):
        if j >= len(key):  # if upper bound
            j = 0  # restart the key from the beginning
        en = (key[j] + num[i])  # add
        num2[i] = en % len(DATABASE)
        j = j + 1
    return int_to_alpha(num2)


def decrypt(plain, key):
    num = alpha_to_int(plain)
    num2 = np.zeros(len(num))
    j = 0
    for i in range(0, len(num)):
        if j >= len(key):  # if upper bound
            j = 0  # restart the key from the beginning
        en = (num[i] - key[j])  # subtract
        num2[i] = en % len(DATABASE)
        j = j + 1
    return int_to_alpha(num2)  # container variable


plain_text = 'ALPHABET'
print(plain_text)
encr = encrypt(plain_text, key)
print(encr)
print(decrypt(encr, key))
