import random
import math

def sigmoid_activation(x):
    return 1 / (1 + math.exp(-x))

input = [1.5, 2.5, -0.5]

weight = [random.uniform(-1, 1) for _ in range(len(input))]
bias = random.uniform(-1, 1)

print(f"Input : {input}")
print(f"Weight : {weight}")
print(f"Bias  : {bias}\n")

total = 0
for i in range(len(input)):
    temp = input[i] * weight[i]
    total += temp
    print(f"Input[{i}] * Weight[{i}] = {temp}")

total += bias
print(f"Total: {total}\n")

output = sigmoid_activation(total)
print(f"Output: {output}")

if output >= 0.5:
    print("Neuron active: Class 1")
else:
    print("Neuron not active: Class 0")