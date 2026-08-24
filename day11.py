#important problems
#1. print numbers from 1 to 10 
for i in range(1,11):
    print(i, end = " ")
print()
list = [2,4,13,52,2,45,23,91,1,78,24,6,18,19,29,39,46,89,87,70,32]
#2. print even numbers from 5 to 30 and above list
for i in range(5, 31):
    if i % 2 == 0:
        print(i,  end =' ')
print()
for x in list:
    if x % 2 == 0:
        print(x, end=' ')
print()
#3. print odd numbers from 5 to 30 and above list
for i in range(5, 31):
    if i % 2 != 0:
        print(i, end = " ")
print()
for x in list:
    if x % 2 != 0:
        print(x, end = " ") 
print()
#4. print numbers divisible by 5 from 1 to 30 and above list
for i in range(1, 31):
    if i % 5 == 0:
        print(i, end = " ")
print()
for x in list:
    if x % 5 == 0:
        print(x, end = " ")
print()
#5. print numbers divisible by both 5 and 7 from 1 to 100 and above list
for i in range(1, 100):
    if i % 5 == 0 and i % 7 ==0:
        print(i, end = " ")
print()
for x in list:
    if x % 5 == 0 and i % 7 ==0:
        print(x, end = " ")
print()
#6. sum of numbers from 10 to 25 and above list
sum = 0
for i in range(10, 26):
    sum += i
print(sum, end = " ")
print()
add = 0
for x in list:
    add += x
print(x, end = " ")
print()
#7. multiplication table of a number 
a = 5
for i in range(1, 11):
    print(f"{a} * {i} = {a*i}")
#8. factorial 
product = 1
n = 5
for i in range(1, n+1):
    product *= i
print(product, end = " ")
print()
#9. fibonacci 
a = 0
b = 1
for i in range(5): 
    next_number = a + b
    print(next_number)
    a = b
    b = next_number
#10. reverse a string
s = "Teja"
print(s[::-1])
print()
#11. count vowels in a string
count = 0
v = "aeiouAEIOU"
s1 = "Lakhinana"
for i in s1:
    if i in v:
        count += 1
print(count)
print()
#12. count z's and y's in a string
s2 = "Python is a programming language and not easy. Zebra"
count2 = 0
target = "yYzZ"
for i in s2:
    if i in target:
        count2 += 1
print(count2)
print()
#13. check whether a number is prime number or not 
num = 29
is_prime = True
if num <= 1:
    print(f"{num} is NOT a prime number.")
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is NOT a prime number.")