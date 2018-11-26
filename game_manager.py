import itertools
import random

class Manager():
    def __init__(self):
        self.deck = []
        for suit in ['Heart', 'Club', 'Diamond', 'Spade']:
            for number in 'AJQK'+''.join(map(str, range(1, 10))):
                self.deck.append((suit, number))
        self.position = 0
        self.dealer = []
        self.player = []
    def draw_one_player(self):
        self.player.append(self.deck[self.position])
        self.position += 1
    def draw_one_dealer(self):
        self.dealer.append(self.deck[self.position])
        self.position += 1
    def start(self):
        random.shuffle(self.deck)
        self.position = 0
        self.dealer = []
        self.player = []
        for _ in range(2):
            self.draw_one_player()
            self.draw_one_dealer()
    def player_totals(self):
        base = sum(int(i) for _, i in self.player if i.isdigit())
        base += sum(10 for _,i in self.player if i in 'JQK')
        a_count = sum(1 for _,i in self.player if i == 'A')
        if a_count:
            options = []
            for option in itertools.product([1,11], repeat=a_count):
                options.append(base + sum(option))
        else:
            options = [base]
        return set(options)
    def winner(self):
        pass
