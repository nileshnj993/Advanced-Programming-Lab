def addMatrix(dict1, dict2, rows,cols):
    sumMatrix = []
    for i in range(rows):
        sumRow = []
        for j in range(cols):
            sumRow.append(dict1[i][j]+dict2[i][j])
        sumMatrix.append(sumRow)   
    return sumMatrix

print('OUTPUT')
print('------')
print('Nilesh Jain - 180953226')
m1 = int(input('Enter number of rows in matrix 1:'))
n1 = int(input('Enter number of columns in matrix 1:'))
m2 = int(input('Enter number of rows in matrix 2:'))
n2 = int(input('Enter number of columns in matrix 2:'))
dict1 = {}
dict2 = {}
if(m1!=m2 or n1!=n2):
    print('Invalid. Enter matrices of same dimension!')
else:
    for i in range(m1):
        row = []
        for j in range(n1):
            val = int(input('Enter non zero value:'))
            row.append(val)
        dict1[i] = row
       
    for i in range(m2):
        row = []
        for j in range(n2):
            val = int(input('Enter non zero value:'))
            row.append(val)
        dict2[i] = row
      
    sumMatrix = addMatrix(dict1,dict2,m1,n1)
    print("\n")
    print("Matrix 1")
    for i in range(m1):
        for j in range(n1):
            if(j==n1-1):
                print(dict1[i][j],end="\n")
            else:
                print(dict1[i][j], end=" ")
    print("\n")
    print("Matrix 2")
    for i in range(m2):
        for j in range(n2):
            if(j==n2-1):
                print(dict2[i][j],end="\n")
            else:
                print(dict2[i][j], end=" ")
   
   
    print("\n")
    print("Resultant Matrix")
    for i in range(m1):
        for j in range(n1):
            if(j==n1-1):
                print(sumMatrix[i][j],end="\n")
            else:
                print(sumMatrix[i][j], end=" ")