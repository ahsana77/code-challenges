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
found = False
lb = int(input("enter a lower bound:"))
ub = int(input("enter an upper bound:"))
for i in range(lb,ub) :
    if i == arm(i) :
        print(i,end=',')
        found = True
if found == False:
        print("no armstrong numbers")
