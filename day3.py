# int
a = 20
print(type(a))
# float
b = 17.05
print(type(b))
# complex
c = 4+5j # here 4 or a number is not mandatory unlike j
print(type(c))
# bool
d = True
print(type(d))
# None type
e = None
print(type(e))
# String
f = "a string"
print(type(f))
# range
g = range(10,15,1)
print(type(g))
# list
h = [10,20,40]
print(type(h))
# tuple
i = (10,20,30,40)
print(type(i))
# set
j = {10,20,30}
print(type(j))
# dictionary
k = {"name" : "sai", "age" : 22}
print(type(k))
# int → float
x = 10
y = float(x)
print(y)          
# float → int
x = 10.5
y = int(x)
print(y)          
# int → string
x = 100
y = str(x)
print(y)         
# string → int
x = "100"
y = int(x)
print(y)         
# string → float
x = "10.5"
y = float(x)
print(y)         
# float → string
x = 10.5
y = str(x)
print(y)         
# list → tuple
x = [1, 2, 3]
y = tuple(x)
print(y)         
# tuple → list
x = (1, 2, 3)
y = list(x)
print(y)         
# list → set
x = [1, 2, 2, 3]
y = set(x)
print(y)           
# set → list
x = {1, 2, 3}
y = list(x)
print(y)          
# string → list
x = "hello"
y = list(x)
print(y)         
# list → string
x = ['a', 'b', 'c']
y = ''.join(x)
print(y)          
# range → list
x = range(1, 6)
y = list(x)
print(y)