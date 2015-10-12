import commodities
import economics
import math
import random
import settings
import pop

class Tile:
    def __init__(self, x, y):
        self.productivity = []
        for i in range(0, settings.resources_n):
            self.productivity.append(random.random())
        self.productivity[1] = 1.0 #HOUSING
        self.productivity[2] = 1.0 #LABOR
        self.x = x
        self.y = y
        self.pop = pop.Pop()
        self.prices = [random.random()] * settings.resources_n
        self.stockpiles = [0] * settings.resources_n
        self.change_in_supply = [0] * settings.resources_n
        self.max_size = 100
        self.births = 0
        self.deaths = 0
        self.imports = 0
        self.exports = 0

    def produce(self):
        for n, x in enumerate(self.productivity):
            if self.pop.n < self.max_size:
                p = x * self.pop.n
            else:
                p = x * self.max_size + math.pow(0.5, (self.pop.n - self.max_size)/ self.max_size )
            self.stockpiles[n] += p
            self.change_in_supply[n] = p

    def consume(self):
        for i in range(0, settings.resources_n):
            consumed = commodities.commodities[i].base_demand * self.pop.n * math.pow(2.0, -1 * self.prices[i] / commodities.commodities[i].consumption_price_halflife)
            self.change_in_supply[i] = self.change_in_supply[i] - consumed #for calculating price

            if consumed > self.stockpiles[i]:
                consumed = self.stockpiles[i]
            self.pop.consumption[i] = consumed
            self.stockpiles[i] = self.stockpiles[i] - consumed
        self.pop.standard_of_living = economics.calculate_standard_of_living(self.pop)

    def reprice(self):
        for i in range(0, settings.resources_n):
            delta_price = -1 * self.change_in_supply[i] / (self.pop.n + 1) * commodities.commodities[i].price_responsiveness
            newprice = self.prices[i] + delta_price
            if newprice < 0:
                newprice = 0.01
            self.prices[i] = newprice
        self.change_in_supply = [0] * settings.resources_n #reset so we can use this method again

    def grow_die(self):
        self.births = 0
        self.deaths = 0
        if self.pop.consumption[0] > self.pop.n * settings.food_per_person: #food_per_person
            births = settings.growth_rate * self.pop.n
            self.births = births
            self.pop.n += births
        elif self.pop.consumption[0] < self.pop.n * settings.food_per_person * 0.9:
            deaths = settings.starvation_rate * self.pop.n
            self.deaths = deaths
            self.pop.n = self.pop.n - deaths

    def cycle(self):
        self.produce()
        self.consume()
        self.reprice()
        self.grow_die()
