def binaryToDecimal(binary):
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
        print("\nNumber: " + str(n) + "\nBinary: " + str(bi) + "\n")
        return n
    else:
        print("Error: not an int")
        raise
