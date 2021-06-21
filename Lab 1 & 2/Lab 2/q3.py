import random

print('OUTPUT')
print('------')
print('Nilesh Jain - 180953226')
print("\n")
dict = {}
n = int(input("Enter number of values:"))
for i in range(n):
    dict[random.randint(0,100)] = input("Enter value:")

sum=0
count=0
string = ""
for key,value in dict.items():
    if(value.isdigit()):
        sum+=int(value)
        count+=1
    else:
        string+=value

print("\n")
print('Average is:', sum/count)
print('Concatenated string is:', string)

found = False
print("\n")
search = input('Enter value to be searched:')
if(search.isdigit()):
    print('Please enter string')
else:
    for key,value in dict.items():
        if(value==search):
            found=True
            print('Element', value, "found at key", key)
    if(found==False):
        print("Element not found!")
    
print('Elements with only special characters:')
for key, value in dict.items():
    special = True
    for i in range(len(value)):
        if(value[i].isalpha() or value[i].isdigit()):
            special = False
            break
    if(special==True):
        print(value)
