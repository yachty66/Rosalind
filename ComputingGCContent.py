"""
prozentualer anteil von C und G in einem string 

get file and iterate over every string and get percentage of CG content and return it with fasta headline

create function 

join lonies list to big string

splitte an jedem >

create dict

go to through list and add from every elem first 14 char to key and rest char as values

iteriere durch values

for every value calculate total len of value / number of CG in the string 

add the result of this calculation as an new value of the value

get pair with highest key value

print [1:] and with line break value
"""

def computigCGContent():
    listWithLines=[]
    linesDict={}
    finalDict={}
    final =""
    percentage=0
    totalCG=0
    with open('ComputingCGContent.txt') as f:
        lines = f.read().splitlines()
        lines = "".join(lines).split(">")
        for i in lines[1:]:
            linesDict.update({i[:13]:i[13:]})
    for k,v in linesDict.items():
        totalCG=v.count("C") + v.count("G")
        percentage=totalCG * 100/len(v)
        linesDict[k] = percentage
    final = max(linesDict, key=linesDict.get) + "\n" + str(max(linesDict.values()))
    return final

    

print(computigCGContent())


    