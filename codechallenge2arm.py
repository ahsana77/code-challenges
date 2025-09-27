# armstrong number :

def arm(num):
    total = 0
    n_str = str(num)
    power = len(n_str)
    for i in n_str :
        dig_pow = int(i)**power
        total = total + dig_pow
    return total

n = int(input("Enter a number:"))
if n == arm(n) :
    print("armstrong number")
else:
    print("not an armstrong number")