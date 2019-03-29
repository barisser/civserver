import gamedata
import settings
import time

queue = []
responses = []
data = gamedata.init()


def main_loop():
    global queue
    global data

    last_iteration = 0
    last_tick = time.time()

    while True:
        if time.time() - last_tick >= settings.logic_interval:
            main_thread(queue, data, last_iteration)
            data, last_iteration = background_thread(data, last_iteration)
            last_tick = time.time()
            

def background_thread(data, last_iteration):
    data['world'].cycle()
    return data, last_iteration


def main_thread(queue, data, last_iteration):
    new_queue = queue
    for i in range(0, len(queue)):
        item = new_queue[i]
        iterate = decide_iterate_or_loop(item, last_iteration)
        if iterate:
            data = process_event(item, data)
            del new_queue[n]
        else:
            break
    return data, new_queue


def decide_iterate_or_loop(item, last_iteration):
    return True


def process_event(item, data):
    global responses #add something to responses
    return data
