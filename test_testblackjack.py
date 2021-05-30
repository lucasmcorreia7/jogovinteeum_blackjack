

__created__= 'By Lucas M.Correia'
__license__= 'FREE'
'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------''
'''
import random
 #  global variables
decks= ("Hearts", "Clubs", "Diamonds", "Spades")
ranking = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values=  {
    "Dois": 2,
    "Tres": 3,
    "Quatro": 4,
    "Cinco": 5,
    "Seis":  6,
    "Sete": 7,
    "Oito": 8,
    "Nove": 9,
    "Dez": 10,
    "Valete": 10,

    "Rainha": 10,
    "Rei": 10,
    "AS": 11
{    #  dictionary
playing = True   #  bool


#  criando a classe cartas
class Card():
    def __init__(self):
        self.suit = suit
        self.ranking = ranking

    def __str__(self):
        self.deck= []
        for suit in suits:
            for ranking in ranking:
          self.deck.append(Card(suit, ranking) #append the card object to self.deck list

    def __dir__(self):
        Deckcomposition = ' ' \
                          ''
