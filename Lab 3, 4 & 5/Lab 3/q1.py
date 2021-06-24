def mulList(numList):
    if(len(numList)==0):
        return None
    product = 1
    for num in numList:
        product*=num
    return product

print('OUTPUT')
print('------')
print('Nilesh Jain - 180953226')

n = int(input('Enter size of list:'))
numList = []
for i in range(n):
    val = int(input('Enter value:'))
    numList.append(val)
    
result = mulList(numList)
if(result==None):
    print('Invalid input!')
else:
    print('The product of the numbers in the list is:', result)