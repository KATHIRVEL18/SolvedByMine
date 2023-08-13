Number = int(input("Enter Any number You Want to find its characteristic :"))

def displayForNotPrime():
    print("the Number {} is not a Prime".format(Number))

def displayForPrime():
    print("the Number {} is a Prime".format(Number))

def Check():
    if Number == 2:
        displayForPrime()

    else:
        i = 2
        while(Number!=i):
            if Number % i == 0:

                displayForNotPrime()
                break

            else:
                displayForPrime()
                break

            i += 1

Check()










