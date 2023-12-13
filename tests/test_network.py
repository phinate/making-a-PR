import numpy as np
import pytest
from neural_network.network import NeuralNetwork


# Test neural network initialization
def test_neural_network_initialization():
    nn = NeuralNetwork(3, 5, 2)
    assert nn.input_size == 3
    assert nn.hidden_size == 5
    assert nn.output_size == 2

    # Check weights initialization
    assert nn.weights_input_to_hidden.shape == (3, 5)
    assert nn.weights_hidden_to_output.shape == (5, 2)


# Test feedforward with valid input
def test_feedforward_valid_input():
    nn = NeuralNetwork(3, 5, 2)
    input_data = np.array([0.5, 0.5, 0.5])
    output = nn.feedforward(input_data)
    assert output.shape == (2,)


# Test error on invalid input data shape
def test_invalid_input_data():
    nn = NeuralNetwork(3, 5, 2)
    with pytest.raises(
        ValueError, match=r"Input data must be a numpy array of shape \(input_size,\)"
    ):
        nn.feedforward(np.array([1, 2]))  # Invalid shape
