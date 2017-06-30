from character import *

types = ["nor", "fir", "wat", "ele", "gra"]

chart = [[1, 1, 1, 1, 1],
        [1, 0.5, 0.5, 1, 2],
        [1, 2, 0.5, 1, 0.5],
        [1, 1, 2, 0.5, 0.5],
        [1, 0.5, 2, 1, 0.5]]

#returns index or None
def isin(item, array): 
    for i in range(0, len(array)):
        if item == array[i]:
            return i
    return None

#(function name array, str(object))
def get_choice(choices, flavour):
    to_print = "Pick " + flavour + ': '
    for i in range(0, len(choices)):
        #appends 'x. choice ' 
        to_print += str(i+1) + '. ' + str(choices[i].name) + ' ' 
    a = ''
    #loops until valid input
    while True: 
        a = input(to_print)
        try:
            if int(a) > 0 and int(a) <= len(choices):
                a = int(a)
                break
            #go back to main menu selection
            elif i == "-1":
                return False 
            else:
                print("Input invalid.")
        except ValueError:
            print("Input invalid.")
    return a 

def do_status(poke):
    if poke.status == 'fnt':
        print(poke.name + " has fainted...")


def calculate(move, poke1, poke2):
    damage = (poke1.level * move.power * (poke1.stats[1] / poke2.stats[2])) / 50 + 2
    multiplier = chart[isin(move.type, types)][isin(poke2.type, types)] #type effectiveness
    
    if multiplier == 0.5:
        print("It's not very effective...")
    elif multiplier == 2:
        print("It's super effective!")
    
    if move.type == poke1.type:
        multiplier = multiplier * 1.5 #adds STAB
    damage = int(multiplier * damage)
    print(poke1.name + " did " + str(damage) + " damage to " + \
        poke2.name)
    poke2.stats[0] -= damage
    if poke2.stats[0] < 0:
        poke2.stats[0] = 0 #limits hp to 0
        poke2.status = 'fnt'
    print(poke2.name + " " + str(poke2.stats[0]) + ", " + \
        str(poke2.copyof[0]))


def fight(poke1, poke2):
    moves = poke1.moves
    a = get_choice(moves, "move") #index of choice +1
    if a == False:
        return a
    else:
        calculate(moves[a-1], poke1, poke2)
        return True

def bag(player):
    print("Oak's words echoed... There's a time and place for"\
        " everything, but not now.")
    return False

def switch(player):
    print("Oak's words echoed... There's a time and place for"\
        " everything, but not now.")
    return False

def run(player, poke2):
    print("Oak's words echoed... There's a time and place for"\
        " everything, but not now.")
    return False


def move(player, poke2):
    a = ''
    go = False
    #loops untl a function runs fully
    while go != True:
        a = input("What will " + player.pokelist[0].name + \
            " do? 1. Fight 2. Bag 3. Pokemon 4. Run ")
        try:
            print(player.name + ': ', end = '') #for debugging
            if int(a) == 1:
                go = fight(player.pokelist[0], poke2)
            elif int(a) == 2:
                go = bag(player)
            elif int(a) == 3:
                go = switch(player)
            elif int(a) == 4:
                go = run(player, poke2)
        except ValueError:
            print("Input invalid")
        #Will only pass if function return is true
        do_status(poke2)  
        if go:
            break
          
    return

def checkwin(array):
    for i in range(0,2):
        current = array[i]
        pokemon = current.pokelist
        for x in range(0, len(pokemon)):
            #if a pokemon is still alive, break out
            if pokemon[x].status != 'fnt': 
                break
            #if all have fainted, return the loser
            elif x == len(pokemon)-1: 
                return array[i]
    return None 

def battle(player, opponent):
    print("Battle initialed!")
    print(opponent.name + ": " + opponent.text)
    go = None
    while go == None:    
        move(player, opponent.pokelist[0])
        print()
        go = checkwin([player, opponent])
        if go != None:
            break
        move(opponent, player.pokelist[0])
        print()
        go = checkwin([player, opponent])
        if go != None:
            break
    print("All of " + go.name + "'s pokemon fainted!")
    if go == player:
        print(player.name + " whited out!")
        print("Unlucky, you were defeated...")
    elif go == opponent:
        print("Congratulations! You defeated " + \
            opponent.name + "!")
        


#TODO faint etc. 