import math
import random
import settings
import pop

class Tile:
    def __init__(self, x, y):
        self.productivity = []
        for i in range(0, settings.resources_n):
            self.productivity.append(random.random())
        self.x = x
        self.y = y
        self.pop = pop.Pop()
        
