

class WashingGroup:
    
    def __init__(self, id):
        self.garments = []
        self.id = id

    
    def addGament(self, newGarment):
        incompativilities = []
        result = []
        for i in range(len(self.garments)):
            if ( self.garments[i].isInompatible(newGarment) and self.garments[i].washTime <= newGarment.washTime ):
                incompativilities.append(i)

            elif ( self.garments[i].isInompatible(newGarment) and self.garments[i].washTime > newGarment.washTime ):
                return [], False

        if ( not self.checkIfItsBetterToInser(incompativilities, newGarment) ):
            return [], False

        for i in incompativilities[::-1]:
            aGarment = self.garments.pop(i)
            result.append(aGarment)

        self.garments.append(newGarment)

        print("grupo {}".format(self.id))
        for g in self.garments:
            print(g.nro)

        return result, True

    def checkIfItsBetterToInser(self,arrIncomp, aGarment):
        totalTime = 0
        for i in arrIncomp:
            totalTime += self.garments[i].washTime
        
        return aGarment.washTime > totalTime

    
    def getGarments(self):
        r = []
        for g in self.garments:
            r.append([g.nro, self.id])

        return r
            
                        



