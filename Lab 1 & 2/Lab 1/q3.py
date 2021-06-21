def dispOdd(listStrings):
    oddString = []
    for string in listStrings:
        if(len(string)%2==1):
            oddString.append(string)
    return oddString

def sameString(listStrings):
    count = 0
    for string in listStrings:
        if(len(string)>=2):
            if(string[0]==string[len(string)-1]):
                count = count+1
    return count    

print('OUTPUT')
print('------')
print('Nilesh Jain - 180953226')
strings = ["test", "Nilesh", "six", "seven", "odd", "even", "racecar"]
print("Strings with odd length -", dispOdd(strings))
print("Number of strings with same starting and ending character -", sameString(strings))