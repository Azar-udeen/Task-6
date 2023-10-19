#Sum of first and last digit of integer 



# Function to find the sum of the first and last digit of an integer
def sum_of_first_and_last_digit(number):
    # Convert the number to a positive integer to handle negative numbers
    number = abs(number)
    
    # Find the last digit (remainder when divided by 10)
    last_digit = number % 10
    
    # Find the first digit by repeatedly dividing by 10 until there's only one digit left
    while number >= 10:
        number //= 10
    
    first_digit = number
    
    # Calculate the sum of the first and last digits
    result = first_digit + last_digit
    
    return result

# Input from the user
num = int(input("Enter an integer: "))

# Calculate and display the result
print("Sum of the first and last digit:", sum_of_first_and_last_digit(num))