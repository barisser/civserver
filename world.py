import settings
import tile

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
