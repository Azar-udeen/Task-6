
#Difference between the number of mangoes


def distribute_mangoes(mangoes, students):
    mangoes.sort()  # Sort the list of mangoes in ascending order.
    min_difference = float('inf')

    for i in range(len(mangoes) - students + 1):
        difference = mangoes[i + students - 1] - mangoes[i]
        if difference < min_difference:
            min_difference = difference

    return min_difference

# Example usage:
N = 6  # Number of bags
M = 3  # Number of students
mangoes = [10, 15, 7, 5, 20, 10]

if M > N:
    print("Not enough bags for all students.")
else:
    result = distribute_mangoes(mangoes, M)
    print("Minimum difference:", result)