#Dictionaries
#Dictionaries are a collection of key-value pairs. They are unordered, mutable, and indexed. They are defined using curly braces {}.
#Creating a dictionary
my_dict = {"name": "Barish", "age": 22, "country": "India"}
print(my_dict)

#Accessing values in a dictionary
print(my_dict["name"]) #Output: Barish

#Adding a new key-value pair to the dictionary
my_dict["hobby"] = "coding"
print(my_dict)

#Updating the value of an existing key
my_dict["age"] = 23
print(my_dict)

#Removing a key-value pair from the dictionary
del my_dict["country"]
print(my_dict)

#Iterating through a dictionary
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

#Practice problem: Create a dictionary of your favorite movies and their release years. Print the release year of your favorite movie.
favorite_movies = {"Inception": 2010, "The Matrix": 1999, "Interstellar": 2014}
print(f"The release year of my favorite movie, Inception, is {favorite_movies['Inception']}.")

# Create a dictionary from these two tuples.
keys = ("name", "age", "city")
values = ("Amit", 22, "Mumbai")
dic= dict(zip(keys,values)) # using zip function
print(dic)
dic= {keys[i]:values[i] for i in range(len(keys))} #using for loop
print(dic)

# Find the key with highest value. Print the key and value.
scores = {"A": 50, "B": 75, "C": 65}
print(max(scores, key=scores.get)) #using max function
scores.get("A") #using get function to get the value
print(scores.get(max(scores, key=scores.get))) #using get function to get the highest value

# Calculate average marks of each student. Print the name of the student with highest average.
data = {
    "Aman": (80, 85, 90),
    "Riya": (70, 60, 75),
    "John": (88, 92, 84)
}
avg=0
b=0
for i in data:
  for j in i:
    avg= sum(data[i])/len(data[i])
  print(i, avg)
if avg > b:
  b+=avg
print(i, b)

nums =[5,2,3,1,2,5,1,2,3]
count={}
for i in nums:
  if i not in count:
    count[i] = 1 # it set the numbers as key and 1 as frequency
  else:
    count[i]+=1 # if the number exist it increases the frequency by 1
print(count)

