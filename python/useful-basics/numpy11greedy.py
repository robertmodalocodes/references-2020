import numpy as np

money = eval(input('Input nominal: \n'))
coinsum = eval(input('Inout number of coins: \n'))
coin = np.zeros(coinsum)

for i in range(0, coinsum):
    coin[i] = input('Take the coin into ' + str(i+1) + ' Rp. ')

# sort by biggest value
coin = -np.sort(-coin)

result = np.zeros(coinsum)
for i in range(0, coinsum):
    result[i] = np.floor(money/coin[i])
    money = np.mod(money, coin[i])  # the remainder of the coin

print('Nominal of coins')
print(coin)
print('Amount of coin')
print(result)
