def maximum(*numbers):
    if(len(numbers)==0):
        return None
    maxNum = numbers[0]
    for i in range(len(numbers)):
        if(numbers[i]>maxNum):
            maxNum = numbers[i];
    return maxNum

val = maximum(10,1,24,12,90)
if(val==None):
    print('Invalid input!')
else:
    print(val)
