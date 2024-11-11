# Function to check if a number is composite
def is_composite(num):
    if num < 4:  # Numbers less than 4 (excluding 1) are not composite
        return False
    for i in range(2, int(num**0.5) + 1):  # Loop up to square root of num
        if num % i == 0:  # If divisible by any number other than 1 and itself
            return True
    return False

# Function to print composite numbers in a given range
def print_composite_numbers(start, end):
    composite_numbers = []
    for num in range(start, end + 1):  # Iterate through the range
        if is_composite(num):  # Check if the number is composite
            composite_numbers.append(num)
    print("Composite numbers:", composite_numbers)  # Print the list of composite numbers

# Example usage
try:
    start = int(input("Enter the starting number: "))  # Input for the starting number
    end = int(input("Enter the ending number: "))  # Input for the ending number
    if start > end:  # Check for invalid range
        print("Starting number should be less than or equal to the ending number.")
    else:
        print(f"Composite numbers between {start} and {end}:")
        print_composite_numbers(start, end)  # Call the function to print composite numbers
except ValueError:  # Handle case where input is not a valid integer
    print("Please enter valid integers for the start and end numbers.")
