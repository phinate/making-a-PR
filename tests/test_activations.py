import pytest
import numpy as np
from neural_network.activation_functions import sigmoid

# Test sigmoid function with scalar input
def test_sigmoid_scalar():
    assert sigmoid(0) == 0.5
    assert sigmoid(100) > 0.99
    assert sigmoid(-100) < 0.01

# Test sigmoid function with numpy array input
def test_sigmoid_array():
    input_array = np.array([-1, 0, 1])
    output_array = sigmoid(input_array)
    expected_output = np.array([1/(1+np.exp(1)), 0.5, 1/(1+np.exp(-1))])
    assert np.allclose(output_array, expected_output)

# Test sigmoid output range
def test_sigmoid_output_range():
    for x in np.linspace(-10, 10, 100):
        assert 0 <= sigmoid(x) <= 1
