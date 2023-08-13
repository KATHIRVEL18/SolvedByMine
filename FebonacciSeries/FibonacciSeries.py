Number = int(input("Enter Any Number to Print Sequence Till :"))

fibList = []
firstTerm = 0
secondTerm = 1
def displayResult():
    print("Fibonacci Series until {} is ".format(Number), fibList)

if Number>=3:
    i = 3

    fibList = [firstTerm, secondTerm]
    while(i<=Number):

        current = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = current

        fibList.append(current)

        i+=1

    displayResult()


else:
    if Number == 1:


        fibList.append(0)
        displayResult()

    else:

        fibList.append(firstTerm)
        fibList.append(secondTerm)
        displayResult()

