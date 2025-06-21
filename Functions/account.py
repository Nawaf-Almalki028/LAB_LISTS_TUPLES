
import System.color as Fore
import cinma_list_tuple_system as clts

def register(username,pass1,pass2):
    if pass1 == pass2:
        print("Welcome to MovieApp")
    else:
        print("Password are not matching")

def login():
    pass

def menu(name):
    while True:
        limitpermissions = False
        if name == "Guest":
            print(
                f"""
                {Fore.Cyan}   Welcome to MovieApp Dear: {name}
                {Fore.Green}|{Fore.Yellow}  please select option from below  {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  1- Show Booked Seats             {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  2- Check seat availability       {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  3- Book a seat                   {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  4- Cancel a booking              {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  5- View stats                    {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  6- View Movies                   {Fore.Green}|
                """
            )
            limitpermissions = True
        elif name != "Guest":
            print(
                f"""
                {Fore.BrightGreen}   Welcome to MovieApp Mr: {name}
                {Fore.Green}|{Fore.Yellow}  please select option from below  {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  1- Show Booked Seats             {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  2- Check seat availability       {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  3- Book a seat                   {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  4- Cancel a booking              {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  5- View stats                    {Fore.Green}|
                {Fore.Green}|{Fore.Yellow}  6- View Movies                    {Fore.Green}|
                """
            )
        optionselected = input("What is your option: ")
        if optionselected == "exit":
            return optionselected
        try:

            if int(optionselected) == 1:
                clts.bockedseatsp()

            elif int(optionselected) == 2:
                print(Fore.BrightYellow+"--------------------------------------")
                gRow = int(input("Enter the Row: "))
                gSeat = int(input("Enter the Seat: "))
                print(Fore.BrightYellow+"--------------------------------------")

                checkstatus = clts.checkavailable(gRow,gSeat)
                if checkstatus == True:
                    print(Fore.BrightYellow+"--------------------------------------")
                    print("  The seats are already booked!")
                    print(Fore.BrightYellow+"--------------------------------------")
                elif checkstatus == False:
                    print(Fore.BrightYellow+"--------------------------------------")
                    print("  The seats are Available!")
                    print(Fore.BrightYellow+"--------------------------------------")

            elif int(optionselected) == 3:
                print(Fore.BrightYellow+"--------------------------------------")
                print("To book a seat complete the Requirements")
                print(Fore.BrightYellow+"--------------------------------------")
                gRow = int(input("Enter the Row: "))
                gSeat = int(input("Enter the Seat: "))
                print(Fore.BrightYellow+"--------------------------------------")

                if gRow <= 10 and gSeat <= 20:
                    checkstatus = clts.bookaseat(gRow,gSeat)
                    if checkstatus == True:
                        print(Fore.BrightYellow+"--------------------------------------")
                        print("  The seats are already booked!")
                        print(Fore.BrightYellow+"--------------------------------------")
                    elif checkstatus == False:
                        print(Fore.BrightYellow+"--------------------------------------")
                        print("  we confirmud your booking!")
                        print(Fore.BrightYellow+"--------------------------------------")
                else:
                    print(Fore.BrightYellow+"--------------------------------------")
                    print(Fore.BrightRed+"The Seats limit is 10 Row and 20 Seats only!")
                    print(Fore.BrightYellow+"--------------------------------------")

            elif int(optionselected) == 4:
                print(Fore.BrightYellow+"--------------------------------------")
                gRow = int(input("Enter the Row: "))
                gSeat = int(input("Enter the Seat: "))
                print(Fore.BrightYellow+"--------------------------------------")

                if gRow <= 10 and gSeat <= 20:
                    checkstatus = clts.cancelseat(gRow,gSeat)
                    if checkstatus == True:
                        print(Fore.BrightYellow+"--------------------------------------")
                        print(Fore.Cyan + " The reservation has been cancelled")
                        print(Fore.BrightYellow+"--------------------------------------")
                    elif checkstatus == False:
                        print(Fore.BrightYellow+"--------------------------------------")
                        print(" The seat isn't booked!")
                        print(Fore.BrightYellow+"--------------------------------------")
                else:
                    print(Fore.BrightYellow+"--------------------------------------")
                    print(Fore.BrightRed+"The Seats limit is 10 Row and 20 Seats only!")
                    print(Fore.BrightYellow+"--------------------------------------")

            elif int(optionselected) == 5:
                clts.viewstatus()

            elif int(optionselected) == 6:
                clts.bonus()



        except:
            print(Fore.BrightYellow+"--------------------------------------")
            print(Fore.Red + "Wrong Input!")
            print(Fore.BrightYellow+"--------------------------------------")


def auth():
    try:
        print(
        f"""
        {Fore.Green}#{Fore.Yellow}        Welcome to MovieApp        {Fore.Green}#
        {Fore.Green}#{Fore.Yellow}  Please select option from below  {Fore.Green}#
        {Fore.Green}#{Fore.Yellow}                                   {Fore.Green}#
        {Fore.Green}#{Fore.Yellow}            1-Sign in              {Fore.Green}#
        {Fore.Green}#{Fore.Yellow}            2-Sign up              {Fore.Green}#
        {Fore.Green}#{Fore.Yellow}        3-Join as a Guest          {Fore.Green}#
        """)

        option = input("Select your option number: ")
        if option == "exit":
            return option
        if int(option) == 1:
            name = input(Fore.BrightCyan + "#-----Username: ")
            password = input(Fore.BrightCyan + "#-----Password: ")
            return int(option),name,password
        
        elif int(option) == 2:
            name = input(Fore.BrightCyan + "#-----Username: ")
            pass1 = input(Fore.BrightCyan + "#-----Password: ")
            pass2 = input(Fore.BrightCyan + "#-----Password: ")
            return int(option),name,pass1,pass2

        elif int(option) == 3:
            return int(option),"a","a"
        
        else:
            print(Fore.BrightYellow+"--------------------------------------")
            print(Fore.Red + "Something went wrong! try again")
            print(Fore.BrightYellow+"--------------------------------------")
            return None
    except:
        print(Fore.BrightYellow+"--------------------------------------")
        print(Fore.Red + "Something went wrong! try again")
        print(Fore.BrightYellow+"--------------------------------------")
        return "issue"
            
