print("1 - Addition")
print("2 - Subtraction")
while True:
    inp = str(input("> "))
    if inp.lower() == "help":
        print("1 - Addition")
        print("2 - Subtraction")
    elif inp == "1":
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        print(num1+num2)
    elif inp == "2":
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        print(num1-num2)
    else:
        print("do you want to continue? ")
        dec = str(input("> "))
        if dec.lower() != "y":
            break
        print("1 - Addition")
        print("2 - Subtraction")
        continue
    print("do you want to continue? ")
    dec = str(input("> "))
    if dec.lower() != "y":
        break
    print("1 - Addition")
    print("2 - Subtraction")