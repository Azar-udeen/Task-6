#Find the minimum element in a rated and shorted list


def find_minimum_element(sorted_list):
    if len(sorted_list) == 0:
        return None  # Return None for an empty list
    else:
        return sorted_list[0]  # The minimum element is the first element in a sorted list

# usage:
sorted_list = [1, 2, 3, 4, 5]
minimum_element = find_minimum_element(sorted_list)
print("The minimum element is:", minimum_element)