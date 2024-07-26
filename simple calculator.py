print("select an operation to perform")
print("1.ADD\n"
      "2.SUBTRACT\n"
      "3.MULTIPLY\n"
      "4.DIVISION\n")
operation=input()
if operation=="1":
    a=int(input("enter a anumber"))
    b=int(input("enter a anumber"))
    print("addition:",a+b)
elif operation=="2":
    a=int(input("enter a anumber"))
    b=int(input("enter a anumber"))
    print("subtraction:",a-b)
elif operation=="3":
    a=int(input("enter a anumber"))
    b=int(input("enter a anumber"))
    print("multiplication:",a*b)
elif operation=="4":
    a=int(input("enter a anumber"))
    b=int(input("enter a anumber"))
    print("division:",a/b)
