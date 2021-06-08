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
            #print(line[2:-1])                  show the string a partir da position [2], like "12Test" will showing "Teste"
            #print(line[line.find(";")+1:-1])   #desta forma não esta engessado, encontrara a posição do primeiro ";" e exibira a partir dele
            vlist = line.split(";")
            print("Date.........: ", vlist[1])
            print("Description..: ", vlist[2])
            print("Department...: ", vlist[3])
    elif option==4:
        break
    option = callupMenu()