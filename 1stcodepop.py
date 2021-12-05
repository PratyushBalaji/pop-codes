print("Options : ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("Type 'quit' or 'exit' to kill the program")
print()
def run():
    print()
    x = input("Option? ")

    if x.lower() == "quit" or x.lower() == "exit":
        print()
        input("Bye ")
        quit()
    elif int(x) == 1:
        y = int(input("Number 1 : "))
        z = int(input("Number 2 : "))
        print(str(y)+" + "+str(z)+" = "+str(y+z))
        run()

    elif int(x) == 2:
        y = int(input("Number 1 : "))
        z = int(input("Number 2 : "))
        print(str(y)+" - "+str(z)+" = "+str(y-z))
        run()

    elif int(x) == 3:
        y = int(input("Number 1 : "))
        z = int(input("Number 2 : "))
        print(str(y)+" × "+str(z)+" = "+str(y*z))
        run()

    elif int(x) == 4:
        y = int(input("Number 1 : "))
        z = int(input("Number 2 : "))
        print(str(y)+" ÷ "+str(z)+" = "+str(y/z))
        run()
    else:
        print("Invalid input, pick again")
        run()
run()
