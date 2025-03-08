def collatz_sequence(n):
    
    while n != 1:
        print(n, end=" ")  # Print the number in the sequence
        if n % 2 == 0:  
            n = n // 2  # If even, divide by 2
        else:
            n = 3 * n + 1  # If odd, multiply by 3 and add 1
    print(n)  # Print the last number (which is always 1)

# Ask the user for input
try:
    num = int(input("Please enter a positive integer: "))
    if num > 0:
        collatz_sequence(num)
    else:
        print("Error: Please enter a positive integer greater than zero.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
