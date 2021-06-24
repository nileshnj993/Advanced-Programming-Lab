import cmath # cmath module deals with complex numbers
def dispVal(n):
    print('Sine value is:', cmath.sin(n))
    print('Square root is:', cmath.sqrt(n))
    print('Log is:', cmath.log(n,10)) # second parameter is base

print('OUTPUT')
print('------')
print('Nilesh Jain - 180953226')

x = int(input('Enter Real Part:'))  
y = int(input('Enter Complex Part:'))
n = complex(x,y)
print('Your complex number is:',n)
dispVal(n)