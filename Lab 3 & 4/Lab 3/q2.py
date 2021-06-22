def uniqueList(numList):
    if(len(numList)==0):
        return None
    unique = set(numList)
    return list(unique)

print('OUTPUT')
print('------')
print('Nilesh Jain - 180953226')

n = int(input('Enter size of list:'))
numList = []
for i in range(n):
    val = int(input('Enter value:'))
    numList.append(val)

result = uniqueList(numList)
if(result==None):
    print('Invalid input!')
else:
    print('The unique elements of the list are:', end = " ")
    for i in range(len(result)):
        if(i==len(result)-1):
            print(result[i])
        else:
            print(result[i], end=" ")
