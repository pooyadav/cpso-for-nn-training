import numpy as np
import matplotlib.pyplot as plt

from neuralNetwork.feedForwardNeuralNetwork import NeuralNetwork
from neuralNetwork.layer import Layer
from src.particleSwarmOptimization.structure.bounds import Bounds


plt.grid(1)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.legend(['error'])
plt.ion()

l_rate = 1.0

bounds = Bounds(-2, 2)

inputLayer = Layer(bounds, size = 2, prev = None, l_rate = l_rate, bias = True, label = "Input layer")
hiddenLayer = Layer(bounds, size = 4, prev = inputLayer, l_rate = l_rate, bias = True, label = "Hidden layer")
outputLayer = Layer(bounds, size = 1, prev = hiddenLayer, l_rate = l_rate, bias = False, label = "Output layer")

fnn = NeuralNetwork()
fnn.appendLayer(inputLayer)
fnn.appendLayer(hiddenLayer)
fnn.appendLayer(outputLayer)

input = np.array([[0, 0],
                  [1, 0],
                  [0, 1],
                  [1, 1]])

target = np.array([[0],
                   [1],
                   [1],
                   [0]])

errors = []

for i in range(20000):
    mod = i % 4
    i_input = np.array([input[mod]])
    fnn.fire(i_input)
    i_target = np.array([target[mod]])
    i_error = fnn.backPropagation(i_target)

    if (i % 500) == 0:
        #print("Error:" + str(fnn))
        errors.append(abs(i_error[0][0]))
        plt.scatter(i, abs(i_error[0][0]))
        plt.pause(0.0001)
        plt.draw()


plt.pause(5)
print(fnn)

print("FIRE: " + str(fnn.fire(np.array([input[0]]))))
print("FIRE: " + str(fnn.fire(np.array([input[1]]))))
print("FIRE: " + str(fnn.fire(np.array([input[2]]))))
print("FIRE: " + str(fnn.fire(np.array([input[3]]))))
