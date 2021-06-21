myList = []

for i in range(1,10):
    myList.append(i)
    for j in range(len(myList)):
        if(j==len(myList)-1):
            print(myList[j], end="\n")
        else:
            print(myList[j], end=" ")