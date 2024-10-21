# read sums.txt

def sum(num1, num2):
    return int(num1) + int(num2)

numbers = open('sums.txt', 'r')

for i in numbers:
    num1, num2 = i.split()
    print(sum(num1, num2))

numbers.close()