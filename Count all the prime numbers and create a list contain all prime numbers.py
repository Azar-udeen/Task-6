
#Count all the prime numbers and create a list contain all prime numbers


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_numbers_in_list(input_list):
    prime_list = []
    prime_count = 0
    for num in input_list:
        if is_prime(num):
            prime_list.append(num)
            prime_count += 1
    return prime_count, prime_list

input_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_count, prime_list = prime_numbers_in_list(input_list)

print("Count of prime numbers:", prime_count)
print("Prime numbers:", prime_list)