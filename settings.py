import commodities

worldx = 80
worldy = 60
average_pop_per_tile = 10
average_money_per_pop = 1.0

food_per_person = 0.5
starvation_rate = 0.1
growth_rate = 0.02

resources_n = len(commodities.commodities)

logic_interval = .5  #seconds

flow_of_money = 0.01  #flow rate, fraction of money spent per interval

migration_coefficient = 0.1
migration_range = 2
migration_randomness = 1.0
