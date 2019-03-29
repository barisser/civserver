import threading

import gamelogic
import server


def server_process():
    server.serve()


def events_process():
    gamelogic.main_loop()


def run():
    server_thread = threading.Thread(target=server_process)
    server_thread.daemon = True
    server_thread.start()

    events_thread = threading.Thread(target=events_process)
    events_thread.daemon = True
    events_thread.start()

    while True:
        k=0


if __name__ == "__main__":
   run()
