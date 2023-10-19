
#Create a two list - one is Even number and another one is odd number


original_list = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = []
odd_numbers = []

for number in original_list:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)