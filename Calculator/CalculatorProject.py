def addition ():
    n = float(input("Enter the number:"))
    b = float(input("Enter the second number:"))
    return n+b

def subtraction ():
    n = float(input("Enter the number:"))
    b = float(input("Enter the second number:"))
    return n-b

def mulitplication ():
    n = float(input("Enter the number:"))
    b = float(input("Enter the second number:"))
    return n*b

def division ():
    n = float(input("Enter the number:"))
    b = float(input("Enter the second number:"))
    return n/b


while True:
    res = []

    print("My Calculator")
    
    print(" Enter 'a' to add")
    print(" Enter 's' to subtract")
    print(" Enter 'm' to multiply")
    print(" Enter 'd' to divide")
    print(" Enter 'q' to quit")
    
    c = input("")

    if c != 'q':
        if c == 'a':
            res = addition()
            print("Answer = ", res)
        elif c == 's':
            res = subtraction()
            print ("Answer = ", res)
        elif c == 'm':
            res = mulitplication()
            print("Answer = ", res)
        elif c == 'd':
            res = division()
            print("Answer = ", res)
    else:
        print("Quitting...")
        break