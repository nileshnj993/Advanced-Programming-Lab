import math

print(abs(-5.2)) # absolute value
print(9/2) # automatic conversion to float - implicit
print(9.0/2)
print(type(1.5)) # prints data type
print(type("lol"))
print(type(True))

# num1 = int(input('Enter no 1:'))
# num2 = int(input('Enter no 2:')) # taking user input
# print(num1+num2)

myList = [1,2,"hello"]
for i in range(len(myList)): # iterating through list
    print(myList[i]) 

print(myList[:]) # printing entire list

myList.append(2) # adding one element at end
myList.extend([4,2,1]) # adding >=1 element at end
print(myList[:])

del myList[2:5] # deleting a string slice
print(myList[:])

print(myList.count(2)) # count no. of occurrences of 2
myList.append(5) 
myList.reverse() # reverse the list
print(myList[:])
print(max("zebra")) # print character with highest ascii value
print(max(myList)) # print largest number in list


dict = { # same as json object - dictionaries are key value pairs
    "name": "Nilesh",
    "age":20
}

print(dict)
print(dict["name"]) # accessing using key

for i in dict:
    print(i,dict[i])
    

testList = [2,3,1,2,7,0]
s = set(testList) # set is a sorted collection of only unique elements ie. no duplicates allowed
print(s)