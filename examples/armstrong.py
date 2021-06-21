def armstrong(n):
    digits = []
    val = n
    while(n>0):
        digits.append(n%10)
        n = int(n/10)

    sum = 0
    for i in range(len(digits)):
        sum+=digits[i]**3

    if(sum==val):
        return True
    else:
        return False

n = int(input("Enter number: "))
if(armstrong(n)):
    print('Armstrong Number!')
else:
    print('Not an Armstrong Number!')