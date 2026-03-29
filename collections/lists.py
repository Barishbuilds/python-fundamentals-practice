#lists
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Accessing elements
print(my_list[0])  # First element
print(my_list[2])  # Third element

# Modifying elements
my_list[1] = 20
print(my_list)

#appending, inserting, removing, popping, reversing, sorting
my_list.append(6)
print(my_list)

my_list.insert(0, 0)
print(my_list)

my_list.remove(3)   
print(my_list)

my_list.pop()
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

#slicing
print(my_list[1:4])  # Slicing from index 1 to 3
print(my_list[:3])   # Slicing from start to index 2
print(my_list[3:])   # Slicing from index 3 to end

#iterating through a list
for item in my_list:
    print(item)

#practice problem: Given a list of integers, create a new list that contains only the even numbers from the original list.
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in original_list:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)


