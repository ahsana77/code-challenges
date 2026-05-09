# calculator

op1 = float(input("Enter number1 :"))
op2 = float(input("Enter number2 :"))

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Modulo\n5.Division\n6.Floor division\n7.Exponentiation")
operation = input("select an operation:")

if operation == '1' or operation == 'Addition':
    result = op1 + op2
    print("Result =",result)
elif operation == '2' or operation == 'Subtraction':
    result = op1 - op2
    print("Result =",result)
elif operation == '3' or operation == 'Multiplication':
    result = op1 * op2
    print("Result =",result)
elif operation == '4' or operation == 'Modulo':
    result = op1 % op2
    print("Result =",result)
elif operation == '5' or operation == 'Division':
    result = op1 / op2
    print("Result =",result)
elif operation == '6' or operation == 'Floor division':
    result = op1 // op2
    print("Result =",result)
elif operation == '7' or operation == 'Exponentiation':
    result = op1 ** op2
    print("Result =",result)
else:
    print("select any given operation")