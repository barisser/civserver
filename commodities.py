commodities = []

class Commodity:
    def __init__(self, name, storeable, living_weight, base_demand, consumption_halflife):
        self.name = name
        self.storeable = storeable
        self.living_weight = living_weight #weighted number repreenting fraction of pop's standard of living
        self.base_demand = base_demand
        self.consumption_halflife = consumption_halflife # price change for consumption to halve (weighted against sum money supply)

food = Commodity('Food', True, 1.0, 10.0, 2.0)
commodities.append(food)

housing = Commodity('Housing', False, 1.0, 5.0, 5.0)
commodities.append(housing)
