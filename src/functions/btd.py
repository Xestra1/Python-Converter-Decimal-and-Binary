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

# Testing
print(binaryToDecimal(1010001, 1)) # returns 81

# EXAMPLE
#    binary number - returns (1 or True) nice formated version or (0 or False) just the number 
#                 ↓  ↓
# binaryToDecimal(n, 1)