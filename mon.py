from moves import *

class pokemon:
    def __init__(self, num, level, moves):
        f = open("pokelist.txt", "r")
        count = 0
        current = []
        while count < num:
            current = f.readline().split()
            count += 1
        self.level = level
        self.type = current[0]
        self.name = current[1]
        self.stats = [int(i) for i in current[2:]]
        self.copyof = [] #list of stats when normal
        for i in range(0, len(self.stats)):
            self.copyof.append(self.stats[i]) 
        
        self.moves = moves 
        self.status = '' #no status effects 

        def replenish(stats, copyof): #heal at pokecentre
            for i in range(0, len(self.stats)):
                self.stats[i] = copyof[i]