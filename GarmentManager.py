from Garment import *
from WashingGroup import *


class GarmentManager:

    def __init__(self):
        self.garments = {}
        self.groups = []


    def createGarments(self):        
        firstProblemFile = open('primer_problema.txt','r')
        lines = firstProblemFile.readlines()
        firstProblemFile.close()

        for line in lines[::-1]:
            if line.startswith("n"):
                n, nGarment, washTime = line.split(" ")
                self.garments[int(nGarment)] = Garment(int(nGarment), int(washTime))
            
            elif line.startswith("e"):
                e, nGarment, nGarmentIncampatible = line.split(" ")
                self.garments[int(nGarment)].addIncompatibleGarment(int(nGarmentIncampatible))



    def sortGarments(self):
        newList = []
        self.garments=sorted(self.garments.items(), key=lambda x: x[1].washTime, reverse=True)
        for g in self.garments:
            newList.append(g[1])

        self.garments = newList
    


    def groupGarments(self):
        self.groups = []
        i = 0
        while( len(self.garments) != 0 ):
            pushOuts = []          
            i += 1
            newGroup = WashingGroup(i)

            for garment in self.garments:
                pushOuts, result = newGroup.addGament(garment)

                if result:
                    self.garments.remove(garment)
                    
                self.garments.extend(pushOuts)
                
            
            self.groups.append(newGroup)
                
                   

    def createSolutionFile(self):
        resultFile = open('solucion.txt','w')
        lines = []
        for g in self.groups:
            lines.extend(g.getGarments())

        lines.sort()
        print(lines)
        resultFile.close()

        

        







g = GarmentManager()
g.createGarments()
g.sortGarments()
g.groupGarments()
g.createSolutionFile()

arr = [1, 2, 3, 4]
for i in arr:
    if i == 2:
        arr.pop(2)

print(arr)
