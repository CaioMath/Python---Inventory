from Funcoes.Funcoes_Arquivos import *

inventory = {}
option = callupMenu()
while (option > 0) and (option < 4):
    if option==1:
        register(inventory)
    elif option==2:
        persist(inventory)
    elif option==3:
        result = view()
        for line in result:
            #print(line[2:-1])                  show the string from that position [2], like "12Test" will show "Test"
            #print(line[line.find(";")+1:-1])   #this way it doesn't get frozen, it will look for the position of the first ";" and will show from that
            vlist = line.split(";")
            print("Date.........: ", vlist[1])
            print("Description..: ", vlist[2])
            print("Department...: ", vlist[3])
    elif option==4:
        break
    option = callupMenu()
