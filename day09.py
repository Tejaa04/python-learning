# 1. If-Elif Condition (HackerRank Problem)
n1 = int(input().strip())

if n1 % 2 != 0:
    print("Weird")
elif 2 <= n1 <= 5:
    print("Not Weird")
elif 6 <= n1 <= 20:
    print("Weird")
else:
    print("Not Weird")


# 2. Leap Year Check
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input())
print(is_leap(year))

# 3. Match-Case Day Mapper
n3 = int(input('Enter the day number: '))

match n3:
    case 1:
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _:
        print('Invalid day number')