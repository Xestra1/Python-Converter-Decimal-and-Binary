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
        return "Error: not an int or number can be presented due to small bit size"
```
binary to decimal
```python
# coming soon
```