def genList(list1, list2):
    list3 = []
    for i in range(len(list1)):
        if(list1[i]%2==1):
            list3.append(list1[i])
    for i in range(len(list2)):
        if(list2[i]%2==0):
            list3.append(list2[i])
    return list3

list1 = [1,2,3,4,5]
list2 = [2,4,5,6,7,8]
print('Nilesh Jain - 180953226')
print(genList(list1,list2))