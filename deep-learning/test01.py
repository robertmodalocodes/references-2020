import numpy as np


def feed_forward(in1, in2, w1, w2, b1):
    hidden = (in1 * w1) + (in2 * w2) + b1
    return hidden


def sigmoid(out):
    out = 1 / (1 + (np.e ** (-(out))))
    return out


z1 = -0.5
z2 = 0.5

weight1 = 0.5
weight2 = 0.1
bias1 = -0.3

print(sigmoid(z1))
print("")
print(sigmoid(z2))

print("")

y = feed_forward(sigmoid(z1), sigmoid(z2), weight1, weight2, bias1)
print("y:")
print(y)
print("")

y_out = sigmoid(y)
print("out y:")
print(y_out)
print('')

error = 1 - y_out
print("error")
print(error)
print('')

# error in output
output_err = error * sigmoid(y_out) * (1 - sigmoid(y_out))
print("output error")
print(output_err)
print('')

# error in hidden
print('hidden neuron 3')
hidden_n3 = weight1 * output_err * \
    sigmoid(sigmoid(z1)) * (1 - sigmoid(sigmoid(z1)))
print(hidden_n3)
print('')

print('hidden neuron 4')
hidden_n4 = weight2 * output_err * \
    sigmoid(sigmoid(z2)) * (1 - sigmoid(sigmoid(z2)))
print(hidden_n4)
print('')


learning_rate = 0.25
# bias and weight correction
delta_w31 = learning_rate * output_err * sigmoid(z1)
delta_w41 = learning_rate * output_err * sigmoid(z2)
delta_b3 = learning_rate * output_err * bias1
print('delta w31', delta_w31)
print('delta w41', delta_w41)
print('delta b3', delta_b3)
