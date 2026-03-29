# Program 1: While loop
i = 1  # initialization

while i <= 5:  # condition
    print(i)
    i += 1  # updation

# As soon as i becomes 6, the loop stops.


# Program 2: For loop
for i in range(1, 9, 2):  # range(start, stop, step)
    print(i)

# The stop value is excluded.


# Program 3: Extract digits from a number (right to left)
number = 5273

while number > 0:
    digit = number % 10
    print(digit)
    number = number // 10


# Program 4: Extract digits from a number (left to right)
number = 5782
temp = number
divisor = 1

# Find divisor
while temp >= 10:
    temp = temp // 10
    divisor = divisor * 10

# Extract digits from left
while divisor > 0:
    digit = number // divisor
    print(digit)
    number = number % divisor
    divisor = divisor // 10


# Program 5: Reverse a list using a while loop
numbers = [1, 2, 3, 4, 5]
length = len(numbers)
reversed_list = []

i = length - 1
while i >= 0:
    reversed_list.append(numbers[i])
    i -= 1

print(reversed_list)