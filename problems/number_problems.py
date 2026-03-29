# Program 1: Armstrong number check (for 3-digit numbers)
number = int(input("Enter a number: "))
temp = number
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** 3
    temp = temp // 10

print(armstrong_sum)

if armstrong_sum == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# Program 2: Palindrome number check
number = int(input("Enter a number: "))
temp = number
reversed_number = 0

while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp = temp // 10

print(reversed_number)

if reversed_number == number:
    print("Palindrome")
else:
    print("Not Palindrome")