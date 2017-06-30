class move:
    def __init__(self, num):
        f = open("movelist.txt", "r")
        count = 0 
        current = []
        while count < num:
            current = f.readline().split()
            count += 1
        self.type = current[0]
        self.name = current[1]
        self.power = int(current[2])
