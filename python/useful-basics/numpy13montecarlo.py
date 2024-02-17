import numpy as np

# applying list comprehension with for loop
sales = np.array([i for i in range(0, 30, 5)])
print(sales)
frequency = np.array([12, 15, 45, 90, 5, 3], dtype='double')
probability = frequency / frequency.sum()
probability = np.round(probability, decimals=2)  # rounding with 2 decimals
cumulative = np.cumsum(probability)  # cumulative
cumulative = cumulative * 100

internal_left = np.zeros([len(sales)])  # left internal
internal_left[1:len(sales)] = cumulative[0:len(cumulative) - 1] + 1
internal_right = cumulative  # right internal

n_prediction = 10
prediction = np.random.random(n_prediction)
prediction = np.round(prediction, 2) * 100
total = 0

for i in range(0, n_prediction):
    for j in range(0, len(internal_left)):
        if prediction[i] >= internal_left[j] and prediction[i] <= internal_right[j]:
            print('Day: {} \t Random Number: {} \t Sales: {}'.format(
                i+1, prediction[i], sales[j]))
            total = total + sales[j]
            break
print('Sales for {} days ahead are {}'.format(n_prediction, total))
