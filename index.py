
a = None
while a == None:
    a_input = input("Enter what A is: ")
    try:
        # convert the input to a number
        a = int(a_input)
    except ValueError:
        # tell the user off
        print("{input} is not a number. Use the number format only.".format(input = a_input))

b = None
while b == None:
    b_input = input("Enter what B is: ")
    try:
        # convert the input to a number
        b = int(b_input)
    except ValueError:
        # tell the user off
        print("{input} is not a number. Use the number format only.".format(input = b_input))

print("Originally your input's were: ", a, ' = a and b = ', b)

print("Now:\n",a, '= b', "\n",b, "= a")