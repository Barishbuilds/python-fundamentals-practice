#Variable naming rules:
#1. Variable names can only contain letters, numbers, and underscores.
#2. Variable names cannot start with a number.
#3. Variable names are case-sensitive.
#4. Variable names cannot be Python keywords.

#Examples of valid variable names:
my_variable = 10
myVariable = 20
my_variable_2 = 30

#camelCase
firstName = "Barish"
lastName = "Mondal"

#snake_case
first_name = "Barish"
last_name = "Mondal"
#These 2 types of variables naming are extensivly used

#Data types in Python:
age = 22 #int
height = 5.9 #float
name = "Barish" #str
is_student = True #bool
hobbies = ["reading", "coding", "traveling"] #list
coordinates = (10, 20) #tuple
person = {"name": "Barish", "age": 30} #dict
print(f"age: {age},\n height: {height},\n name: {name},\n is_student: {is_student},\n hobbies: {hobbies},\n coordinates: {coordinates},\n person: {person}")

#Type conversion:
marks = input("Enter a number")
print(marks)
print(type(marks)) #By default, input() returns a string

marks = int(marks) #Converting the string input to an integer
print(marks) #Now marks is an integer
print(type(marks)) #Now it will show <class 'int'>

#Using End parameter in print function:
print("Hello", end=" ") #This will print "Hello" and stay on the same line
print("World!") #This will print "World!" on the same line as "Hello"   



