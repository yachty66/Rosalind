def read():
    currStr=""
    listWithOrderedReads=[]
    with open('OverlapGraphs.txt') as f:
        lines = f.read().splitlines()
        counter = 0
        for i in lines:
            counter += 1
            if i[0] == ">" and counter != 1:
                listWithOrderedReads.append(currStr)
                currStr=""
                currStr=currStr + i
            else:
                currStr=currStr + i
        listWithOrderedReads.append(currStr)
    return listWithOrderedReads

def createDict():
    dictWithHeadAndString = {}
    for i in read():
        dictWithHeadAndString.update({i[1:14]:i[14:]})
    return dictWithHeadAndString

def output():
    lastThreeChar=""
    listEdges = []
    for k,v in createDict().items():
        lastThreeChar=v[-3:]
        for k2, v2 in createDict().items():
            if k2 != k:
                if lastThreeChar==v2[:3]:
                    listEdges.append(k)
                    listEdges.append(k2)

    listEdges=[listEdges[x:x+2] for x in range(0, len(listEdges), 2)]
    for i in listEdges:
        for j in listEdges:
            if i != j:
                if(i[0] in j):
                    if(i[1] in j):
                        listEdges.remove(j)

    
    for i in listEdges:
        print(i[0] + " " + i[1])
    
        
        



            


print(output())
            


           