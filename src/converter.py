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
        return bi, n
    else:
        print("Error: not an int")

def decimalToBinary(num):
    if (num > 0):
        nu = num
        b = ""
        for x in range(num):
            if num > 0.9:
                t = num % 2
                num /= 2
                b = b + str(math.floor(t))
            else:
                break
        nb = b.rstrip("0")
        return nu, int(str(nb)[::-1])
    else:
        print("Error: not an int")