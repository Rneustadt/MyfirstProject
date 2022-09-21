def getInput ():
    myinput = input ('pick a number between one and ten - \n')
    print ('ok you picked' + str(myinput ))
    return myinput

def getResult (myFirstNumber,mySecondNumber):
    print (myselection)
    if myselection == '+' or myselection == '-' or myselection ==  '*' or myselection ==  '/':
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
        print ('faild')
        return 'wrong selection'
    

print ('Lets add numbers')     # this is a comment
myFirstNumber = int (getInput())
mySecondNumber = int (getInput())
myselection = input('choose opperation')
print ('you selected ' + myselection) 
result = getResult(myFirstNumber, mySecondNumber)
print (result)