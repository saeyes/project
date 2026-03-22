# matchmaking.py

import time

class Player:
    def __init__(self, name, mmr):
        self.name = name
        self.mmr = mmr
        self.queue_time = time.time()

def matchmaking(players):
    matches = []
    players.sort(key=lambda x: x.mmr)

    while len(players) >= 2:
        p1 = players.pop(0)
        best = None

        for p2 in players:
            wait = time.time() - p2.queue_time
            allowed = 100 + wait * 10

            if abs(p1.mmr - p2.mmr) < allowed:
                best = p2
                break

        if best:
            players.remove(best)
            matches.append((p1, best))

    return matches