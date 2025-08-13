# Create an empty list
my_list = []

# Append elements: 20, 30, 40, 50
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)

# Insert 25 at the second position (index 5)
my_list.insert(5, 25)

# Extend with another list: [70, 80, 90]
my_list.extend([70, 80, 90])

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find and print the index of the value 50
index_of_50 = my_list.index(50)
print("Index of 50:", index_of_50)
