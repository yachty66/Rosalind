codontab = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",  "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop", "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def rnaToProtein():
    with open('rosalind_prot.txt') as f:
        lines = f.readlines()
        rna = lines[0]
    proteinList = ""
    while(True):
        if len(rna) < 3:
            break 
        firstThreeProtein = ""
        firstThreeProtein = rna[:3]
        for k in codontab:
            if k == firstThreeProtein:
                if codontab[k] == "Stop":
                    break
                proteinList = proteinList + codontab[k]
        rna = rna[3:]
    return proteinList


print(rnaToProtein())
    



