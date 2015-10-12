commodities = []

class Commodity:
    def __init__(self, name, storeable, living_weight, base_demand, price_responsiveness, consumption_price_halflife):
        self.name = name
        self.storeable = storeable
        self.living_weight = living_weight #weighted number repreenting fraction of pop's standard of living
        self.base_demand = base_demand
        self.price_responsiveness = price_responsiveness
        self.consumption_price_halflife = consumption_price_halflife

food = Commodity('Food', True, 1.0, 10.0, 1, 1.0)
commodities.append(food)

housing = Commodity('Housing', False, 1.0, 5.0, 1, 1.0)
commodities.append(housing)
