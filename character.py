from mon import *
#from items import * 

class person:
    def __init__(self, name, text):
        self.name = name
        self.text = text

class trainer(person):
    def __init__(self, name, text, pokemon, items):
        person.__init__(self, name, text)
        self.pokelist = pokemon
        self.bag = items

class player(trainer):
    def __init__(self, name, pokemon, items):
        trainer.__init__(self, name, '', pokemon, items)

    