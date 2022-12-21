from matplotlib import pyplot as plt

def collatz(n):

    '''This function returns a list of all the numbers in the collatz sequence
    and a plot for visualization for a given scalar'''

    assert type(n) == int, 'Expected int; however {} was provided'.format(type(n))
    numList = [n]

    def getnum(n):

        #Check the even case
        if n % 2 == 0:
            n = int(n / 2)
            numList.append(n)
            return n

        #Check the odd case
        elif n % 2 == 1:
            n = 3 * n + 1
            numList.append(n)
            return n

    # Check the 1 case
    while n != 1:
        n = getnum(int(n))

    #Plot and return the results
    plt.plot(numList)
    return numList

# Test the function
collatz(27)