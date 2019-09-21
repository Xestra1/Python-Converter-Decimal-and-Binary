# Decimal to Binary
A basic decimal to binary converter that is built in python

# code 
decimal to binary
```python
import math

def decimalToBinary(num):
    if (num > 0):
        nu = num
        b = ""
        for x in range(num):
            t = num % 2
            num /= 2
            b = b + str(math.floor(t))
        nb = b.rstrip("0")
        return "\nNumber: " + str(nu) + "\nBinary: " + str(nb[::-1]) + "\n"
    else:
        return "Error: not an int"
```
binary to decimal
```python
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
```