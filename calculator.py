#This program is to make calculator

def add(num1, num2):
    return num1 + num2


print('Enter numbers to find the sum: ')
n1 = int(input('Enter the first number : ')) 
n2 = int(input('Enter the first number : ')) 

sum = add(n1, n2)
print(f'The sum of {n1} and {n2} is {sum}')