while True:
    x = (input("enter first number = "))

    if x == "stop":
        break
    else:
        Y = int(x)

    x2 = int(input("enter second number = "))

    op = input("enter operater (+ , - , * , / ) = ")

    if op == "*":
        x3 = Y * x2 
        print(x3)

    elif op == "+":
        x4 = Y + x2
        print(x4)

    elif op == "-":
        x5 = Y - x2
        print(x5)

    elif op == "/":
        x6 = Y / x2
        print(x6)

    else:
        print("the operation is incorrect")
("login features in features branch (feature branch)")