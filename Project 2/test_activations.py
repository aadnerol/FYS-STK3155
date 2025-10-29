import numpy as np

# Importer funksjonene fra activations.py
from activations import (
    relu, relu_deriv,
    sigmoid, sigmoid_deriv,
    leaky_relu, leaky_relu_deriv,
    linear, linear_deriv,
    softmax
)

def test_sigmoid():
    print("Testing sigmoid and its stability...")
    z = np.array([[-100.0, 0.0, 100.0]])
    # Sammenlign med "naiv" definisjon — skal være numerisk lik
    expected = 1 / (1 + np.exp(-z))
    actual = sigmoid(z)
    assert np.allclose(actual, expected, atol=1e-10, rtol=1e-10), "Sigmoid values mismatch"

    # Derivatet skal være s*(1-s)
    s = sigmoid(z)
    expected_der = s * (1 - s)
    actual_der = sigmoid_der(z)
    assert np.allclose(actual_der, expected_der, atol=1e-10, rtol=1e-10), "Sigmoid derivative mismatch"
    print("✅ Sigmoid passed\n")

def test_relu():
    print("Testing ReLU and its derivative...")
    z = np.array([-1.0, 0.0, 1.0])
    expected_relu = np.array([0.0, 0.0, 1.0])
    expected_der = np.array([0.0, 0.0, 1.0])

    assert np.allclose(relu(z), expected_relu), "ReLU values mismatch"
    assert np.allclose(relu_deriv(z), expected_der), "ReLU derivative mismatch"
    print("✅ ReLU passed\n")

def test_softmax():
    print("Testing softmax normalization...")
    z = np.array([[1.0, 2.0, 3.0]])
    s = softmax(z)
    # Summen over klasser skal være 1 for hver batch
    sums = np.sum(s, axis=1)
    assert np.allclose(sums, np.ones_like(sums)), "Softmax rows do not sum to 1"
    print("✅ Softmax passed\n")

if __name__ == "__main__":
    print("Running activation function tests...\n")
    test_sigmoid()
    test_relu()
    test_softmax()
    print("All tests passed successfully 🎉")
