from itertools import combinations
from game import Game
from player import Cooperative, Cheater, Copycat, Grudger, Detective, Imposter

if __name__ == '__main__':
    g = Game()
    pl = [Cooperative(), Cheater(), Copycat(), Grudger(), Detective(), Imposter()]
    for (p1, p2) in combinations(pl, 2):
        g.play(p1, p2)
    for (k, v) in g.top3(7):
        print(k, v)
