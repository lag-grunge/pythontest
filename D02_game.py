from collections import Counter

class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        turn1 = turn2 = "coop"
        res1 = 0
        res2 = 0
        for match in range(self.matches):
            turn1, turn2 = player1.next_turn(turn2, self.matches), player2.next_turn(turn1, self.matches)
            if turn2 == "coop" and turn1 == "coop":
                res1, res2 = res1 + 2, res2 + 2
            elif turn2 == "cheat" and turn1 == "cheat":
                res1, res2 = res1, res2
            elif turn2 == "coop" and turn1 == "cheat":
                res1, res2 = res1 + 3, res2 - 1
            else:
                res1, res2 = res1 - 1, res2 + 3
        self.registry[player1] += res1
        self.registry[player2] += res2
        player1.reset()
        player2.reset()

    # simulate number of matches
    # equal to self.matches

    def top3(self):
        return self.registry.most_common(3)
    # return top three
