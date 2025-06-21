import Functions.account as act
import Functions.datasys as dts
import System.color as Fore

file = "Data/users.json"
while True:
    def callauth():
        x = act.auth()
        if x == "exit":
            exit()

        accounting(x)

    def accounting(x):
        try:
            if x[0] == 1:
                getuser = dts.founduser(file,x[1],x[2])
                if getuser[0] == True:
                    act.menu(getuser[1])
                else:
                    print("Wrong username or password!")
                    callauth()
            if x[0] == 2:
                if x[2] == x[3]:
                    Username = x[1]
                    Password = x[2]
                    print(x)
                    dts.adduser(file,x[1],x[2])
                    act.menu(x[1])
                else:
                    print("Password Dosen't Match! ")
                    callauth()
            if x[0] == 3:
                act.menu("Guest")
        except:
            print(x)
            print("Error!")
            callauth()

    callauth()