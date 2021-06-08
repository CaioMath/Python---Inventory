def callupMenu():
    choice = int(input("Enter: "

    "\n<1> To register an asset"

    "\n<2> To persist a file"

    "\n<3> To view the stored assets"
                    
    "\n<4> To exit: "))
    return choice

def register(vdictionary):
    aswer = "YES"
    while aswer=="YES":
        vdictionary[input("Enter the asset number: ")]= [
            input("Enter the date of the last upgrade: "),
            input("Enter the description: "),
            input("Enter the department: ")]
        aswer = input("Type <YES> to continue.").upper()

def persist(vdictionary):
    with open("inventory.csv", "a") as inv:
        for vkey, vvalue in vdictionary.items():
            inv.write(vkey + ";" + vvalue[0] + ";" +
                      vvalue[1] + ";" + vvalue[2] + "\n")
    return "Persisted successfully!"

def view():
    with open("inventory.csv", "r") as inv:
        lines = inv.readlines()
    return lines