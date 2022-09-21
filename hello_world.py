def getInput ():
    myinput = input ('pick a number between one and ten - \n')
    print ('ok you picked' + str(myinput ))
    return myinput

def getResult (myFirstNumber,mySecondNumber):
    if myselection == '+':
        return  int(myFirstNumber) + int(mySecondNumber)
    elif myselection =='-':
        return  int(myFirstNumber) - int(mySecondNumber)
    elif myselection =='*':
        return  int(myFirstNumber) * int(mySecondNumber)
    elif myselection =='/':
        return  int(myFirstNumber) / int(mySecondNumber)
    elif myselection =='%':
        return  int(myFirstNumber) % int(mySecondNumber)
    else:
        print ('wrong selection')

print ('Lets add numbers')     # this is a comment
myFirstNumber = int (getInput())
mySecondNumber = int (getInput())
myselection = input('choose opperation')
print ('you selected ' + myselection) 
result = getResult(myFirstNumber, mySecondNumber)
print (result)