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

for b in range(1, 100):
    print(decimalToBinary(b))