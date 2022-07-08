import numpy as np

def matrixMethod():
    
    dnaStrings=[]
    firstCharacters =[]
    A = 0
    C = 0
    G = 0
    T = 0
    with open('ConsensusAndProfile.txt') as f:
        lines = f.read().splitlines()
        
        for i in lines:
            if i[0] == ">":
                dnaStrings.append(i[0])
            else:
                dnaStrings.append(i)
        dnaStrings = "".join(dnaStrings).split(">")
        dnaStrings = dnaStrings[1:]
        lenDnaString = len(dnaStrings[0])
    matrix = np.zeros((4,lenDnaString))
    
    for i in range(lenDnaString):
        for j in dnaStrings:
            firstCharacters.append(j[i])

        A = firstCharacters.count("A")
        C = firstCharacters.count("C")
        G = firstCharacters.count("G")
        T = firstCharacters.count("T")
        firstCharacters=[]

        for k in range(4):
            if k == 0:
                matrix[k, i] = A
            elif k == 1:
                matrix[k, i] = C
            elif k == 2:
                matrix[k, i] = G
            elif k == 3:
                matrix[k, i] = T
    return matrix

def getConsensusString():
    matrix = matrixMethod()
    indexOfHighestValues = []
    for i in range(len(matrix[0])):
        maxV = max(matrix[:, i])
        counter = 0
        val = 0
        for j in matrix[:, i]:
            if j == maxV:
                val = counter
            counter += 1
        indexOfHighestValues.append(str(val))
    indexOfHighestValues = list(map(lambda x: x.replace("0", "A"), indexOfHighestValues))
    indexOfHighestValues = list(map(lambda x: x.replace("1", "C"), indexOfHighestValues))
    indexOfHighestValues = list(map(lambda x: x.replace("2", "G"), indexOfHighestValues))
    indexOfHighestValues = list(map(lambda x: x.replace("3", "T"), indexOfHighestValues))
    finalStr = "".join(indexOfHighestValues)

    A=""
    for i in list(matrix[0].astype(int)):
        A= A+" "+str(i)
    A = "A:" + A

    C=""
    for i in list(matrix[1].astype(int)):
        C= C+" "+str(i)
    C = "C:" + C

    G=""
    for i in list(matrix[2].astype(int)):
        G= G+" "+str(i)
    G = "G:" + G

    T=""
    for i in list(matrix[3].astype(int)):
        T= T+" "+str(i)
    T = "T:" + T

    final = finalStr + "\n" + A+ "\n" + C+ "\n" + G+ "\n" + T        
    return final  

print(getConsensusString())


