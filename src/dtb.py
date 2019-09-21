import math

def decimalToBinary(num):
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
            b = b + str(math.floor(t))
        # strips the other 0s
        nb = b.rstrip("0")
        return "\nNumber: " + str(nu) + "\nBinary: " + str(nb[::-1]) + "\n"
    else:
        return "Error: not an int"

for b in range(1, 100):
    print(decimalToBinary(b))