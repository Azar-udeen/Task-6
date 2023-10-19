#find the non-repeating element 


def find_first_non_repeating(nums):
    count_dict = {}
    
    # Count the occurrences of each number
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find the first non-repeating element
    for num in nums:
        if count_dict[num] == 1:
            return num

    # If there are no non-repeating elements, return None
    return None

# Example usage
my_list = [4, 2, 7, 2, 5, 4, 6]
result = find_first_non_repeating(my_list)
if result is not None:
    print("The first non-repeating element is:", result)
else:
    print("No non-repeating elements found in the list.")