# Arthematic operations
print(10 + 5 * 2)          # 20
print(2 ** 3 ** 2)         # 512, ** follows right to left 
print(10 // 3)             # 3
print(10 % 3)              # 1
print(5 / 2)               # 2.5
print([1,2,3] + [4,5,6])   # [1,2,3,4,5,6]
print((1,2,3) + (4,5,6))   # (1,2,3,4,5,6)
print({1,2,3} + {4,5,6})   # error, because set operation doest have '+'
print([1,2,3] * 4)         # [1,2,3,1,2,3,1,2,3]
print(*[1,2,43])           # 1 2 43, * in print function is used for unpacking
print([1,2,3] + (1,2,3))   # error, we cannot add list to a tuple
print([1,2,3] + 'dog')     # error we cannot add list to a string

#Relational and Logical Operators
print(10 > 5 and 20 < 30)   # True
print(10 > 20 and 5 < 10)   # False
print(not 1 == 1)           # False
print(1 < 2 < 3)            # True
print(1 > 2 > 3)            # False
print('abc' > 'def')        # False
print([1,2,3] < [1,3,4])    # True, stops at [1] because the conditon was satisfied

# assignment and walrus operator
print(a=10)                 # error
print(a:=10)                # 10, this is a walrus operator
if (n := 34) > 10:
   print(n)                 # True

# Identity and equality operators
a = [1,2,3] 
b = [1,2,3]
print(a==b)        # True
print(a is b)      # True
a = 'abc'
b = 'abc'
print(a==b)        # True
print(a is b)      # True
a = (1,2,3)
b = (1,2,3)
print(a == b)      # True
print(a is b)      # True

# Membership operator
a = [1,2,3,4,5]    
print(6 in a)       # False
print(6 not in a)   # True
print('abc' in 'abcde')  # True