
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
        print("\nNumber: " + str(nu) + "\nBinary: " + str(nb[::-1]) + "\n")
        return nu
    else:
        print("Error: not an int")
        raise

# I don't know what's the purpose of this so I'm just gonna comment it out.        
"""
for b in range(1, 100):
    print(decimalToBinary(b))
"""
