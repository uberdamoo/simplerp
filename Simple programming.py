#Simple RP
	#A program made to simplfy the roleplaying process
"""
1:Allow User Input
user = input('What do you want to say to me?  ')
print ('You said', User, '.')
2:Check User Input
user = input('What do you want to say to me?  ')
if len(user) > 0:
    print ('You said', user, '.')
else:
    print ('type something next time')
3:Time to talk to a function
def user(text):
    "prints what the user passes to function"
    print (text)
    return
4:Let's have the command line keep asking?
number = 2
while (number < 99):
    user = input('What do you want to say to me?  ')
    if len(user) > 0:
        print ('You said', user, '.')
    else:
        print ('type something next time')
5:Let's ask for input and send it to a file
"""
#creates file and works, but does not write to the file if f is not closed.
#also time is a tuple? doesn't concatanate?
import time
f = open('roleplayhistory.txt', 'a')
number = 2
while (number < 3):
    user = input('What do you want to say to me?  ')
    if len(user) > 0:
        print ('You said', user, '.')
        f.write(str(time.localtime()) + '\n') #needs structering
        f.write(user + '\n')
        f.close()
        number = number +2
    else:
        print ('type something next time')
