def genPattern(n):
    count = 1
    rows = 0
    while(rows<n):
        for i in range(n):
            rows = rows+1
            for j in range(i+1):
                if(j==i):
                    print(count,end = "\n")
                else:
                    print(count,end = " ")
                count = count+1

print('OUTPUT')
print('------')
print('Nilesh Jain - 180953226')
genPattern(5)