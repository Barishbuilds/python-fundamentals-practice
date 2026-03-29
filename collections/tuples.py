#Tuples
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

#Tuples are immutable, so we cannot change their elements
# tuple1[0] = 10 #This will raise a TypeError 
    
#However, we can create a new tuple by concatenating existing tuples
tuple2 = (6, 7, 8)
tuple3 = tuple1 + tuple2
print(tuple3)

#We can also repeat tuples using the * operator
tuple4 = tuple1 * 2
print(tuple4)

#Tuples can contain elements of different data types
mixed_tuple = (1, "Hello", 3.14, [1, 2, 3], (4, 5))
print(mixed_tuple)

#We can access tuple elements using indexing and slicing
print(tuple1[0]) #Output: 1
print(tuple1[1:4]) #Output: (2, 3, 4)

#Tuples support unpacking
a, b, c, d, e = tuple1
print(a, b, c, d, e) #Output: 1 2 3 4 5

#Tuples have some built-in methods
print(tuple1.count(2)) #Output: 1
print(tuple1.index(3)) #Output: 2

#practice problem: Create a tuple of your favorite fruits and print the second fruit in the tuple.
fruits = ("Apple", "Banana", "Cherry", "Date", "Elderberry")
print(fruits[1]) #Output: Banana

# Print the length of the tuple. Check if 30 exists in the tuple.
tu= (10,20,30,40,50)
n= len(tu)
for i in range (n):
  if tu[i] == 30:
    print("30 exists")
print("The length of the tuple is", n)

# Given a list of int, print the sum of all the even elements in it
a= [1,2,3,4,5,6,7,8]
n= len(a)
even=[]
s=0
for i in range(n):
  if (a[i] % 2 == 0):
    s+= a[i]
    even.append(a[i])
print(f"Even elements: {even}")
print(f"Sum of even elements: {s}")
