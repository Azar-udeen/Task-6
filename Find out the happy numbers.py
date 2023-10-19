#Find out the happy numbers 


def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

def count_happy_numbers(numbers):
    count = 0
    for num in numbers:
        if is_happy_number(num):
            count += 1
    return count

# Your list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

happy_count = count_happy_numbers(numbers)
print("Number of Happy Numbers in the list:", happy_count)