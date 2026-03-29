#functions

#syntax
def greet():
  print("Hello Friends")

greet()

#function with parameters
def greet(name):
  print(f"Hello {name}")
greet("Barish") 

#function with return value
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
    
def power(a, b):
    return a ** b

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_fib)
        return fib_sequence
    
def is_armstrong(n):
    temp = n
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** 3
        temp = temp // 10
    return armstrong_sum == n

def is_palindrome(n):
    temp = n
    reversed_number = 0
    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp = temp // 10
    return reversed_number == n

def remove_duplicates(d):
    d1 = {}
    temp = []
    for i in d:
        if i not in temp:  # if the key is not in temp
            if d[i] not in temp:  # if the value is not in temp
                temp.append(d[i])  # appending the value in temp so that it can filter out the duplicates
                d1[i] = d[i]  # assigning the values to their keys in a blank dic
    return d1

def main():
    print(add(5, 3))
    print(subtract(5, 3))
    print(multiply(5, 3))
    print(divide(5, 3))
    print(power(5, 3))
    print(factorial(5))
    print(gcd(48, 18))
    print(lcm(48, 18))
    print(is_prime(29))
    print(fibonacci(10))
    print(is_armstrong(153))
    print(is_palindrome(12321))
    d = {"a":1, "b":2, "c":1, "d":3}
    print(remove_duplicates(d))

if __name__ == "__main__":
    main()

