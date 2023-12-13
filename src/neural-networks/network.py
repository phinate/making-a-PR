import numpy as np
from .activation_functions import sigmoid

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights
        self.weights_input_to_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.weights_hidden_to_output = np.random.randn(self.hidden_size, self.output_size)

    def feedforward(self, input_data):
        if not isinstance(input_data, np.ndarray) or input_data.shape[0] != self.input_size:
            raise ValueError("Input data must be a numpy array of shape (input_size,)")
        hidden = sigmoid(np.dot(input_data, self.weights_input_to_hidden))
        output = sigmoid(np.dot(hidden, self.weights_hidden_to_output))
        return output
