# Sample lists (you can replace these with your own lists)


list1 = [1, 2, 3, 4, 5, 3]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9, 5]

# Find duplicates using sets
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Find duplicates in all three lists
common_duplicates = set1.intersection(set2, set3)

# Convert the set back to a list
result = list(common_duplicates)

# Print the duplicates
print("Duplicates in the three lists:", result)