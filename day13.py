PIN = 2004
attempt = 3
while attempt > 0:
    user_input = int(input("Enter your pin: "))  
    if user_input == PIN:
        print("Correct pin")
        break
    else:
        print(f"Incorrect, {attempt-1} tries left")
    attempt -= 1

# count digits
n = int(input("Enter a number to count the digits: "))
count = 0
while n > 0:
    n //= 10
    count += 1
print(count)

# Reversing a number and checking whether its a palindrome
num = 1234
rev = 0 
while num > 0:
    last_digit = num % 10
    rev = (rev * 10) + last_digit
    num //= 10
print(f"num is {num}")
print(f"Reversed number is {rev}")
if num == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Armstrong number
n1 = 153
count = (len(str(n1)))
temp = n1
sum = 0

while n1 > 0:
    dig = temp % 10
    sum += dig ** count
    temp //= 10
if sum == n1:
    print("Armstrong number")

else:
    print("Not an Armstrong number")

# string palindrome
def is_palindrome(name):
    left = 0
    right = len(name) - 1

    while left < right:
        if name[left] != name[right]:
            return False
        left += 1
        right -= 1
    return True

name = "madam"
print(is_palindrome(name))