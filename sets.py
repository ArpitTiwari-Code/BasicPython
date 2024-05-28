# Creating a set
my_set = {1, 2, 3, 4, 5}

# Printing the set
print("Original Set:", my_set)

# Adding an element to the set
my_set.add(6)
print("After adding 6:", my_set)

# Removing an element from the set
my_set.remove(3)
print("After removing 3:", my_set)

# Checking membership
print("Is 2 in the set?", 2 in my_set)

# Set operations
other_set = {4, 5, 6, 7, 8}
print("Union of sets:", my_set.union(other_set))
print("Intersection of sets:", my_set.intersection(other_set))
print("Difference of sets:", my_set.difference(other_set))
