import itertools
import random


class Manager():
    def __init__(self):
        '''
        Adds the cards to the deck.
        '''
        self.deck = []
        for suit in ['Heart', 'Club', 'Diamond', 'Spade']:
            for number in 'AJQK'+''.join(map(str, range(2, 10))):
                self.deck.append((suit, number))
        self.position = 0
        self.dealer = []
        self.player = []

    def draw_one(self, player=True):
        '''
        Used to draw one random card from the remaining cards in the deck.
        Doesn't check if there are any remaining cards in the deck, so will
        crash if the there are no remaining cards in the deck. Parameter player
        is used to determine which hand to put the card in. True to add to the
        players hand, and False to add to the dealers.
        '''
        hand = [self.dealer, self.player][int(bool(player))]
        hand.append(self.deck[self.position])
        self.position += 1

    def start(self):
        '''
        Used to initialise the game. It shuffles the deck and empties hands.
        '''
        random.shuffle(self.deck)
        self.position = 0
        self.dealer = []
        self.player = []
        for hand in [False, True] * 2:
            self.draw_one(hand)

    def totals(self, player=True):
        '''
        Used to return a list of potential hand totals less than 21. It returns
        an empty list if the hand can only be above 21. Parameter player is used
        to determine which hand to check. True to get totals for player hand,
        and False to get totals for dealer hand.
        '''
        hand = [self.dealer, self.player][int(bool(player))]
        base = sum(int(i) for _, i in hand if i.isdigit())
        base += sum(10 for _, i in hand if i in 'JQK')
        a_count = sum(1 for _, i in hand if i == 'A')
        if a_count:
            options = []
            for option in itertools.product([1, 11], repeat=a_count):
                options.append(base + sum(option))
        else:
            options = [base]
        return list(filter(lambda x: x <= 21, set(options)))

    def winner(self):
        '''
        Returns the winner. Its draws cards for the dealer while they are under
        17. It then checks if either is bust, then compares. In the case of
        both having the same highest(below 22) score then the dealer wins.
        '''
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
