# this is needed!
import math

def decimalToBinary(num, tf):
    # checks if int
    if (num > 0):
        # used for return
        nu = num
        b = ""
        # goes through the number
        for x in range(num):
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
            return nu, int(nb)
    else:
        print("Error: not an int")
        raise

# This is for testing
for b in range(1, 20):
    print(decimalToBinary(b, 1))

# EXAMPLE
#    decimal number - returns (1 or True) nice formated version or (0 or False) just the binary 
#                 ↓  ↓
# decimalToBinary(b, 1)