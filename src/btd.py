import math

def binaryToDecimal(binary):
    if (binary > 0):
        bi = binary
        strbi = str(binary)
        strbi = strbi[::-1]
        n = 0
        p = 0
        for x in strbi:
            if (int(x) == 1):
                n = n + (2 ** p)
                p += 1
            elif (int(x) == 0):
                p += 1
        return "\nNumber: " + str(n) + "\nBinary: " + str(bi) + "\n"
    else:
        return "Error: not an int"