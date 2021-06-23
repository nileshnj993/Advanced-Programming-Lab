from time import localtime, strftime

def displayGreeting(username):
    now = int(strftime("%H", localtime()))
    greeting =""
    if(now>5 and now<12):
        print('Good Morning', username)
    elif(now>12 and now<16):
        print('Good Afternoon', username)
    elif(now>16 and now<20):
        print('Good Evening', username)
    else:
        print('Good Night', username)

username = input('Enter Username: ')
displayGreeting(username)
