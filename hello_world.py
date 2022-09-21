def getInput ():
    myinput = input ('pick a number between one and ten - \n')
    return myinput

print ('Lets add numbers')     # this is a comment
myFirstNumber = int (getInput())
print ('ok you picked' + str(myFirstNumber ))
mySecondNumber = int (getInput())
print ('ok you picked' + str(mySecondNumber))
myselection = input('choose opperation')
print ('you selected ' + myselection) 
result = ''
if myselection == '+':
   result = int(myFirstNumber) + int(mySecondNumber)
elif myselection =='-':
    result = int(myFirstNumber) - int(mySecondNumber)
elif myselection =='*':
    result = int(myFirstNumber) * int(mySecondNumber)
elif myselection =='/':
    result = int(myFirstNumber) / int(mySecondNumber)
elif myselection =='%':
    result = int(myFirstNumber) % int(mySecondNumber)
else:
    print ('wrong selection')
print (result)