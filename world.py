import random
import settings
import tile
import world_queries

class World:
    def __init__(self):
        self.map = []
        self.cities = []
        for x in range(0, settings.worldx):
            r = []
            for y in range(0, settings.worldy):
                q = tile.Tile(x, y)
                r.append(q)
            self.map.append(r)

    def cycle(self):
        b = 0
        d = 0
        for x in range(0, settings.worldx):
            for y in range(0, settings.worldy):
                self.map[x][y].cycle()
                b += self.map[x][y].births
                d += self.map[x][y].deaths
        print "BIRTHS: "+str(b)
        print "DEATHS: "+str(d)
        self.migration()

    def migrate_tiles(self, source_tile_coords, dest_tile_coords, n):
        if self.map[source_tile_coords[0]][source_tile_coords[1]].pop.n > 0:
            if self.map[source_tile_coords[0]][source_tile_coords[1]].pop.n < 1:
                n = self.map[source_tile_coords[0]][source_tile_coords[1]].pop.n
            money_transfer = n / self.map[source_tile_coords[0]][source_tile_coords[1]].pop.n * self.map[source_tile_coords[0]][source_tile_coords[1]].pop.money
            m = self.map[source_tile_coords[0]][source_tile_coords[1]].pop.n
            if m < n:
                n = m
            self.map[source_tile_coords[0]][source_tile_coords[1]].pop.n = self.map[source_tile_coords[0]][source_tile_coords[1]].pop.n - n
            self.map[dest_tile_coords[0]][dest_tile_coords[1]].pop.n = self.map[dest_tile_coords[0]][dest_tile_coords[1]].pop.n + n

            self.map[source_tile_coords[0]][source_tile_coords[1]].pop.money = self.map[source_tile_coords[0]][source_tile_coords[1]].pop.money - money_transfer
            self.map[dest_tile_coords[0]][dest_tile_coords[1]].pop.money = self.map[dest_tile_coords[0]][dest_tile_coords[1]].pop.money + money_transfer

    def migration(self):
        s = 0
        for x in range(0, settings.worldx):
            for y in range(0, settings.worldy):
                my_sol = self.map[x][y].pop.standard_of_living
                best_neighbor = [x, y, my_sol]
                neighbors = []
                for i in range(-1*settings.migration_range, settings.migration_range):
                    for j in range(-1*settings.migration_range, settings.migration_range):
                        neighbors.append([x+i, y+j, -9999])
                for n, neighbor in enumerate(neighbors):
                    if neighbor[0] >= 0 and neighbor[0]< settings.worldx and neighbor[1] >= 0 and neighbor[1] < settings.worldy:
                        nx = neighbor[0]
                        ny = neighbor[1]
                        neighbors[n][2] = self.map[nx][ny].pop.standard_of_living * random.random()*settings.migration_randomness - settings.migration_randomness * 0.5
                        if neighbors[n][2] > best_neighbor[2]:
                            best_neighbor = neighbors[n]

                sol_diff = best_neighbor[2] - my_sol
                if sol_diff > 0.0001:
                    n = settings.migration_coefficient * sol_diff / (my_sol + best_neighbor[2]) * self.map[x][y].pop.n
                    s += n
                    self.migrate_tiles([x, y], [best_neighbor[0], best_neighbor[1]], n)
        print str(s)+" MIGRATING"
        print "TOTAL POP: "+str(world_queries.total_pop())
