"""
finding longest string
read all the strings from the lines into a list 
get all substrings of current string and add this substring to a list 


read lines where every line is an item in a list
create two lists
iterate over list and get every substring from an elem and add them to a list if done add this list to an list
iterate over last created list twice and 

ich muss einen string aus einer liste nehmen und schauen ob der string in den darauffolgenden listen vorkommt 
wenn ja kann ich den string speichern 
dafuer muss ich jedes strng durch gehen und checken ob der curr string in diesem vorkommt 
dafuer kann ich eine helper funktion bauen - diese bekommt immer eine liste welche verschiedene str enthaelt und returnt dann truye oder false
dann kann ich durch alle strings itern und mir zurueck geben lassene 

helper nimmt curr string und curr list und return bool 
wenn bool false gehe direk zum  nachsten elem
wenn elem durch fuege elem zu commonlist



liste mit strings
nehm erstes elem und ersten char davon
gehe zu zweiten elem in liste und pruefe ob char vorkommt 
wenn ja gehe liste weiter
wenn char in jeder liste vorkommmt fuege char in eine liste mit commonstrings ein und gehe zurueck zu erstem elem und diesmal nehme den char + den naechsten 
wenn der char einmal nicht vorkommmen sollte gehe zurueck zu erster liste und nehme naechsten charact
"""
def read():
    currStr=""
    listWithOrderedReads=[]
    with open('FindingASharedMotif.txt') as f:
        lines = f.read().splitlines()
        counter = 0
        for i in lines:
            counter += 1
            if i[0] == ">":
                listWithOrderedReads.append(currStr)
                currStr=""
                #currStr=currStr + i
            else:
                currStr=currStr + i
        listWithOrderedReads.append(currStr)
        listWithOrderedReads = listWithOrderedReads[1:]
    return listWithOrderedReads

def checkIfStringAppears(s, l):
    #wenn s min einmal in einem string vorkommt true else false
    counter = 0 
    for i in l:
        if s in i:
            counter += 1
    if counter > 0:
        return True
    else:
        return False

def out():
    print(read())
    currList=[]
    check = True
    finalCheck = True 
    allList=[]
    listCommonSubstrings=[]
    for i in read():
        for j in range(len(i)):
            currList.append(i[:j+1])
        allList.append(currList)
        currList=[]
    for i in allList:
        print(allList)
        for j in i:
            for k in allList:
                print("k")
       

    print(listCommonSubstrings)

print(out())