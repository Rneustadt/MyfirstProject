def getInput ():
    myinput = input ('pick a number between one and ten - \n')
    print ('ok you picked' + str(myinput ))
    return myinput

def getResult (myFirstNumber,mySecondNumber,op):
    print (op)
    if op == '+' or op == '-' or op ==  '*' or op ==  '/':
        if op == '+':
            return  int(myFirstNumber) + int(mySecondNumber)
        elif op =='-':
            return  int(myFirstNumber) - int(mySecondNumber)
        elif op =='*':
            return  int(myFirstNumber) * int(mySecondNumber)
        elif op =='/':
            return  int(myFirstNumber) / int(mySecondNumber)
        elif op =='%':
            return  int(myFirstNumber) % int(mySecondNumber)
    else:
        print ('faild')
        return 'wrong selection'
    
def runCalc ():
    print ('Lets add numbers')     # this is a comment
    myFirstNumber = int (getInput())
    mySecondNumber = int (getInput())
    myselection = input('choose opperation')
    print ('you selected ' + myselection) 
    result = getResult(myFirstNumber, mySecondNumber, myselection)
    print (result)

runCalc ()
