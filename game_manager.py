import itertools
import random

class Manager():
    def __init__(self):
        self.deck = []
        for suit in ['Heart', 'Club', 'Diamond', 'Spade']:
            for number in 'AJQK'+''.join(map(str, range(2, 10))):
                self.deck.append((suit, number))
        self.position = 0
        self.dealer = []
        self.player = []

    def draw_one(self, player=True):
        hand = [self.dealer, self.player][int(bool(player))]
        hand.append(self.deck[self.position])
        self.position += 1

    def start(self):
        random.shuffle(self.deck)
        self.position = 0
        self.dealer = []
        self.player = []
        for hand in [False, True] * 2:
            self.draw_one(hand)

    def totals(self, player=True):
        hand = [self.dealer, self.player][int(bool(player))]
        base = sum(int(i) for _, i in hand if i.isdigit())
        base += sum(10 for _,i in hand if i in 'JQK')
        a_count = sum(1 for _,i in hand if i == 'A')
        if a_count:
            options = []
            for option in itertools.product([1,11], repeat=a_count):
                options.append(base + sum(option))
        else:
            options = [base]
        return list(filter(lambda x: x<=21, set(options)))

    def winner(self):
        player_total = self.totals(True)
        dealer_twist = True
        while dealer_twist:
            dealer_total = self.totals(False)
            if dealer_total and min(dealer_total) < 17:
                self.draw_one(False)
            else:
                dealer_twist = False
        if not player_total:
            return 'DEALER'
        if not dealer_total:
            return 'PLAYER'
        if max(player_total) > max(dealer_total):
            return 'PLAYER'
        else:
            return 'DEALER'
