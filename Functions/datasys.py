import json
import System.color as Fore

def loaddata(file):
    with open(file,"r") as f:
        return json.load(f)

def savedata(file,data):
    try:
        with open(file,"r") as f:
            OldData = json.load(f)

        OldData.update(data)

        with open(file,"w") as f:
            json.dump(OldData,f,indent=4)
    except:
        OldData = {}
        OldData.update(data)
        with open(file,"w") as f:
            json.dump(OldData,f,indent=4)

def founduser(file,name,password):
    with open(file,"r") as f:
        data = json.load(f)

    for i in data:
        if data[i]["name"] == name and data[i]["password"] == password:
            print("sucess")
            logicx = True
            break
        else:
            logicx = False
    return logicx,name

def adduser(file,name,password):
    with open(file,"r") as f:
        data = json.load(f)

    for i in data:
        print(i)
        x = i
    x = int(x) + 1
    data = {f"{x}": {'name': f'{name}', 'password': f"{password}"}}
    savedata(file,data)
    
# {'2243': {'name': 'a3', 'age': 23}, '23': {'name': 'a3', 'age': 23}}