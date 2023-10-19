
#Find a sub-list with sum equal to zero


def has_sublist_with_zero_sum(lst):
    for i in range(len(lst)):
        current_sum = 0
        for j in range(i, len(lst)):
            current_sum += lst[j]
            if current_sum == 0:
                return True
    return False

my_list = [4, 2, -3, 1, 6]
result = has_sublist_with_zero_sum(my_list)
if result:
    print("There is a sub-list with a sum equal to zero.")
else:
    print("There is no sub-list with a sum equal to zero.")