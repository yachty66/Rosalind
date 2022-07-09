"""
given is sequence of dna strings
find biggest common string 

take first char from first elem and check if this char appears in all other lists
if yes add to list common strings and repeat process with char+nextcharsacter
if no go to next char and repeat process 
if done with string go to next elem and repeat till no elements 


bilden von allen substrings is to calc intense. 

actually i just need to create substrings of one string 
check this time how long it does take to do that
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

def createSubStrings():
    currStr = []
    allStr =[]
    for i in read():
        for j in range(len(i)):
            for k in range(len(i)):
                currStr.append(i[:k+1])
            i = i[1:]
        allStr.append(currStr)
        print(currStr)
        currStr = []
    return allStr

def check(str, l):
    if l.count(str) == 0:
        return False
    else:
        return True

def out():
    '''
    commonStr l
    iter list
    iter list
    all function mit last elem 
    if all true add last elem to commonstr 
    return longest elem  

    iter over list 
    create methods which takes j and k 
    in method check if j is in k and return  bool
    for all k with j 
    if all is true add to commonstrings
    return max frpom cs
    '''
    commonStr = []
    for i in createSubStrings():
        for j in i:
            if all([check(j, l) == True for l in createSubStrings()]):
                commonStr.append(j)
    return max(commonStr)

            
            
print(out())