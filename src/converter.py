# this is needed!
import math

def binaryToDecimal(binary, tf):
    # checks if its a int
    if (binary > 0):
        # used for return statement
        bi = binary
        # reverses the binary 
        strbi = str(binary)
        strbi = strbi[::-1]
        n = 0
        p = 0
        # goes through all of the 1s and 0s
        for x in strbi:
            # code for 1
            if (int(x) == 1):
                n = n + (2 ** p)
                p += 1
            # code for 0
            elif (int(x) == 0):
                p += 1
        if (tf == True):
            return "\nNumber: " + str(n) + "\nBinary: " + str(bi) + "\n"
        elif (tf == False):
            return n
        else:
            return bi, n
    else:
        print("Error: not an int")

def decimalToBinary(num, tf):
    # checks if int
    if (num > 0):
        # used for return
        nu = num
        b = ""
        # goes through the number
        for x in range(num):
            x = x
            # takes the reminder
            t = num % 2
            # divdes by 2
            num /= 2
            # the binary
            b = b + str(math.floor(t))
        # strips the other 0s
        nb = b.rstrip("0")
        if (tf == True):
            return "\nNumber: " + str(nu) + "\nBinary: " + str(nb[::-1]) + "\n"
        elif (tf == False):
            return nb
        else:
            #          --THIS IS NEEDED--
            return nu, int(str(nb)[::-1])
    else:
        print("Error: not an int")