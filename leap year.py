print("Check if it is a leap year")

while True:
    user_input = input("Enter a year (type 'exit' to exit): ")

    if user_input.lower() == "exit":
        break

    try:
        year = int(user_input)
        lpc1 = year % 4

        if lpc1 != 0:
            print("Not a leap year")
        elif lpc1 == 0:
            lpc2 = year % 100

            if lpc2 != 0:
                print("This is a leap year")
            elif lpc2 == 0:
                lpc3 = year % 400

                if lpc3 != 0:
                    print("This is not a leap year")
                elif lpc3 == 0:
                    print("This is a leap year")
                else:
                    pass
            else:
                pass
        else:
            pass

    except ValueError:
        print("Invalid input. Please enter a valid year or type 'exit' to exit.")

