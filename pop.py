import json
import random
import settings

class Pop:
    def __init__(self):
        self.n = float(random.randint(0, settings.average_pop_per_tile*2))
        self.money = random.randint(0, settings.average_money_per_pop*2*self.n)
        self.consumption = [0] * settings.resources_n
        self.standard_of_living = 1.0
