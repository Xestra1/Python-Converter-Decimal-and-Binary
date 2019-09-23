# Python Converter Decimal and Binary
A basic decimal to binary converter that is built in python

## decimal to binary
```python
# EXAMPLE
#    decimal number - returns (1 or True) nice formated version or (0 or False) just the binary 
#                 ↓  ↓
# decimalToBinary(b, 1)

import math

def decimalToBinary(num, tf):
    if (num > 0):
        nu = num
        b = ""
        for x in range(num):
            t = num % 2
            num /= 2
            b = b + str(math.floor(t))
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
```

## binary to decimal
```python
# EXAMPLE
#    binary number - returns (1 or True) nice formated version or (0 or False) just the number 
#                 ↓  ↓
# binaryToDecimal(n, 1)

def binaryToDecimal(binary, tf):
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
        if (tf == True):
            return "\nNumber: " + str(n) + "\nBinary: " + str(bi) + "\n"
        elif (tf == False):
            return n
        else:
            return bi, n
    else:
        print("Error: not an int")
        raise
```