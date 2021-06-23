import math # math module deals with real numbers

def dispVal(n):
    print('Sine value is:', math.sin(n))
    print('Square root is:', math.sqrt(n)) 
    print('Log is:', math.log(n,10)) # second parameter is base

print('OUTPUT')
print('------')
print('Nilesh Jain - 180953226')

n = int(input('Enter number:'))
dispVal(n)