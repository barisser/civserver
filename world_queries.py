import gamelogic
import Image
import json
import jsonpickle
import settings

def tile_query(x, y):
    x = int(x)
    y = int(y)
    t = gamelogic.data['world'].map[x][y]
    tjson = json.loads(jsonpickle.encode(t))
    return tjson

def pop_map():
    a = []
    w = gamelogic.data['world']
    for x in w.map:
        s = []
        for y in x:
            q = y.pop.n
            s.append(q)
        a.append(s)
    return a

def total_pop():
    n = 0
    for x in gamelogic.data['world'].map:
        for y in x:
            n += y.pop.n
    return n
