import json
import jsonpickle
import gamelogic

def tile_query(x, y):
    x = int(x)
    y = int(y)
    t = gamelogic.data['world'].map[x][y]
    tjson = json.loads(jsonpickle.encode(t))
    return tjson
