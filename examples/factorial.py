def fact(n):
    product = 1
    while(n>1):
        product*=n
        n = n-1
    return product

n = int(input('Enter number: '))
print(n,"!=",fact(n))