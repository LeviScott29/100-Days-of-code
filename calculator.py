def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+": add,
    "-":subtract,
    "*":multiply,
    "/":divide}

end="no"
print("Welcome to the calculator!")
while end =="no":
    while True:
        try:
            num1= float(input("what's the first number?: "))
            break
        except ValueError:
            print("invalid input only accepts numbers")
    while True:
        try:
            num2= float(input("what's the second number?: "))
            break
        except ValueError:
            print("invalid input only accepts numbers")

    for symbol in operations:
        print(symbol)
        
    while True:
        operation_symbol = input("pick an operation from the line above: ")
        if operation_symbol in operations:
            break
        else: print("operation not valid only pick from list above")
    
    calculation=operations[operation_symbol]
    answer= calculation(num1,num2)
    print (answer)
    
    while True:
        allowed_words= ["exit", "start over", "continue"]
        outer_choice=input("do you want to exit, start over, or continue?" )

        if outer_choice in allowed_words:
            break
        else: print(" you can only choose 'exit', 'start over' or 'continue'")
            
    if outer_choice == "exit":
        end="yes"
    elif outer_choice =="start over":
        continue
    elif outer_choice =="continue":
        while True:
            
            while True:
                try:
                    num3=float(input("choose another number: "))
                    break
                except ValueError:
                    print("invalid input only accepts numbers")

            for symbol in operations:
                print(symbol)
            while True:
                operation_symbol = input("pick an operation from the line above: ")
                if operation_symbol in operations:
                    break
                else: print("invalid operation pick only from the list above")


            calculation=operations[operation_symbol]
            answer= calculation(answer,num3)
            print (answer)
            
            while True:
                allowed_words= ["exit", "start over", "continue"]
                inner_choice=input("do you want to exit, start over, or continue?: ")
                if inner_choice in allowed_words:
                    break
                else: print(" you can only choose 'exit', 'start over' or 'continue'")
            if inner_choice == "exit":
                end="yes"
                break
            elif inner_choice =="start over":
                break
            elif inner_choice =="continue":
                continue
                        
    
    
