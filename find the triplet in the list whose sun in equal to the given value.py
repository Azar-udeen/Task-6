#find the triplet in the list whose sun in equal to the given value 


 def find_triplet_with_sum(arr, target):
    arr.sort()  # Sort the input list

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                # Triplet found
                return [arr[i], arr[left], arr[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    # No triplet found
    return None

# Example usage:
my_list = [10, 20, 30, 9]
target_value = 59
result = find_triplet_with_sum(my_list, target_value)

if result:
    print("Triplet with the given sum:", result)
else:
    print("No triplet found with the given sum")