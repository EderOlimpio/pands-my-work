def sqrt(N):
    # We should raise an error if the number is not positive
    if N <= 0:
        raise ValueError("Input must be a positive number.")
    
    # Initial guess, can be N/2 or any positive number
    guess = N / 2.0
    
    # Define tolerance for approximation
    tolerance = 1e-6  # The smaller the tolerance, the more accurate the result
    
    # Iterate to improve the guess
    while True:
        # Newton's method formula
        new_guess = 0.5 * (guess + N / guess)
        
        # Check if the difference between the new guess and old guess is smaller than tolerance
        if abs(new_guess - guess) < tolerance:
            break
        
        # Update guess for the next iteration
        guess = new_guess
    
    return new_guess

# Main function to interact with the user
if __name__ == "__main__":
    try:
        number = float(input("Please enter a positive number: "))
        # Get the square root approximation
        result = sqrt(number)
        print(f"The square root of {number} is approx. {result:.6f}.")
    except ValueError as e:
        print(e)

# References:
# Newton's Method (Wikipedia) - URL: https://en.wikipedia.org/wiki/Newton%27s_method
# Numerical Methods: A Practical Approach by S. S. Sastry: Citation: Sastry, S. S. (2003). Numerical Methods: A Practical Approach. Prentice Hall.
# Introduction to Numerical Analysis by Francis B. Hildebrand: Citation: Hildebrand, F. B. (1987). Introduction to Numerical Analysis. Dover Publications.
# Python Documentation: Iterative Methods: URL: https://docs.python.org/


