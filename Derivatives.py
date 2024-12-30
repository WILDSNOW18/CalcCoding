import sympy as sp

# Define the variable
x = sp.symbols('x')

def compute_derivative(function_str):
    # Parse the input function
    function = sp.sympify(function_str)

    # Compute the derivative with respect to x
    derivative = sp.diff(function, x)

    return derivative

# Example usage:
# Enter the function as a string, e.g., '3*sin(x)**2' or 'x**2 + 3*x + 2'
function_str = input("Enter the function f(x): ")
result = compute_derivative(function_str)

print(f"The derivative of f(x) = {function_str} is: {result}")
