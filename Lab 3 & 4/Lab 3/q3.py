# QUESTION 3 - Count number of local variables in a function
def countLocal():
    global a
    global b
    a = 2 # global
    b = "test" # global
    c = 23 # local
    d = "local" # local
    
print('OUTPUT')
print('------')
print('Nilesh Jain - 180953226')

print('Number of local variables in the function are:',countLocal.__code__ .co_nlocals)