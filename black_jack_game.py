from random import *

suits = ('Hearts','Diamonds','Spades','clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two' : 2,'Three' : 3,'Four' : 4,'Five' : 5,'Six' : 6,'Seven' : 7,'Eight' : 8,'Nine' : 9,'Ten' : 1,'Jack' : 10,'Queen' : 10,'King' : 10,'Ace' : 11}
play = True
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:

    def __init__(self):

        self.all_cards = []
        for suit in suits:
            for rank in ranks:

                cards = Card(suit,rank)
                self.all_cards.append(cards)

    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()

        return 'the deck has: '+deck_comp

    def suffle(self):
        shuffle(self.all_cards)

    def pop_one(self):
        return self.all_cards.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_to_ace(self):
        while self.value > 21 and self.aces: # self.aces or self.aces > 0 cause 0 is take by default as false
            self.value -= 10
            self.aces -= 1


#test_deck = Deck()
#test_deck.suffle()

#test_player = Hand()
#test_player.add_card(test_deck.pop_one())
#print(test_deck.pop_one())
#print(test_player.value)


class Chips:
    def __init__(self,total = 100):
        self.total = total
        self.bat = 0

    def win_bat(self):
        self.total += self.bat

    def lose_bat(self):
        self.total -= self.bat


def take_bet(chips):
    while True:
        try:
            chips.bat = int(input('pleas enter the amount of chips you want to bet'))
        except:
            print('please enter the inter value')
        else:
            if chips.bat > chips.total:
                print(f'you dont have enough amount {chips.total}')
            else:
                break

def hit(deck,hand):

    singal_Card = deck.pop_one()
    hand.add_card(singal_Card)
    hand.adjust_to_ace()

def hit_or_stand(deck,hand):
    global play
    while True:
        x = input('hit or stand! enter h or s')

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('player stand ,Dealer turn')
            play = False
        else:
            print('sorry! i dont under stand')
            continue

        break

def show_some(player,dealer):
    print('dealers hand:')
    print('one card hidden!')
    print(dealer.cards[1])
    print(('\n'))
    print('players hand')
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print('dealers hand:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('players hand:')
    for card in player.cards:
        print(card)

def player_busts(player,dealer,chips):
    print('plsyer lose')
    chips.lose_bat()

def player_win(player,dealer,chips):
    print('player win')
    chips.win_bat()

def dealer_bust(player,dealer,chips):
    print('dealer lose')
    chips.lose_bat()

def dealer_win(player,dealer,chips):
    print('dealer win')
    chips.win_bat()

def push(player,dealer):
    print('tie')


while True:

    print('Welcom to Black Jack')

    deck = Deck()
    deck.suffle()

    player_hand = Hand()
    player_hand.add_card(deck.pop_one())
    player_hand.add_card(deck.pop_one())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.pop_one())
    dealer_hand.add_card(deck.pop_one())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while play:
        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_bust(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_win(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)


    print(f'player total chips are {player_chips.total}')

    newgame = input('if you want to paly again put y other wise n')

    if newgame[0].lower() == 'y':
        play = True
        continue
    else:
        break







