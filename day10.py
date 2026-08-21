list = [4, 3, 2, 5, 6]
#print elements in list with for each loop
for i in list:
    print(i)
#print elements in list with index based for loop
for i in range(0, len(list)):
    print(list[i])
#skip printing even numbers in list
for i in list:
    if i % 2 != 0:
        print(i)
#skip printing odd numbers in list
for i in list:
    if i % 2 == 0:
        print(i)
#when number 2 comes stop printing  
for i in list:
    if i == 2:
        break
    print(i)
#when first odd number comes stop printing
for i in list:
    if i % 2 != 0:
        break
    print(i)
#print numbers from 1 to 10, when all numbers are printed, print 'All numbers printed'
for i in range(1,11):
    print(i)
print("All numbers are printed")
#print numbers from 1 to 10, skipping even numbers, when all numbers are printed, print 'All numbers printed'
for i in range(1, 11):
    if i %2 != 0:
        print(i)
print('All numbers printed')
#print numbers from 10 to 1, when 5 comes stop printing, when all numbers are print, print 'All numbers printed'
for i in range(10, 0, -1):
    if i != 5:
        print(i)
    else:
        break
print('All numbers printed')