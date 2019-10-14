# Python Converter Decimal and Binary
A basic decimal to binary converter that is built in python

## using the inputs and outputs
Open input.txt and put in your binary or decimal numbers. Then, Answer the input(s). dtb is decimal to binary and btd is binary to decimal.

## Benchmarking
- specs
    - I5 8600k
    - 32GB of ram
- 1-10
    - 0.0050 seconds - B-D
    - 0.0018 seconds - D-B - Before optimizations
    - 0.0018 seconds - D-B - After optimizations
- 1-100
    - 0.0025 seconds - B-D
    - 0.0044 seconds - D-B - Before optimizations
    - 0.0024 seconds - D-B - After optimizations
- 1-10000
    - 0.0816 seconds - B-D
    - 47.7646 seconds - D-B - Before optimizations
    - 0.093 seconds - D-B - After optimizations

## functions
### decimal to binary
The files for this code can be found in the src and functions files.

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
            if num > 0.9:
                t = num % 2
                num /= 2
                b = b + str(math.floor(t))
            else:
                break
        nb = b.rstrip("0")
        if (tf == True):
            return "\nNumber: " + str(nu) + "\nBinary: " + str(nb[::-1]) + "\n"
        elif (tf == False):
            return nb
        else:
            return nu, int(nb)
    else:
        print("Error: not an int")
```

### binary to decimal
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