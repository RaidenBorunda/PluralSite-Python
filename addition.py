#Creating our addition function
def addition(a, b):
    return a + b
    
#Main Program
num1 = float(input('Enter your number:\n'))
num2 = float(input('Enter your number:\n'))
#Calling our function
result = addition(num1, num2)
print('The result is', result)