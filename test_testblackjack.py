

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
        DeckComposition = ''   #set the deck comp as an empty string
          for card in self.deck:
               deckComposition  += '/n'  + card.__str__()  # Card class string representation
            return  " the deck has:  " + deckComposition

    def shuffle (self):
        random.shuffle(self.deck)

        # grab the deck attribute of Deck class then pop off card item from list and set it to single card
        def deal (self):
            singleCard = self.deck.pop()
            return singleCard



# testing everything so far
# testDeck = Deck()
# testDeck.shuffle()
# print(testDeck)

# create hand class: grabbing the single card and adding to someon's hand
class Hand():
     def __init__(self):
         self.cards = [] # start with 0 cards in hand
         self.values= 0  #starting with 0 value
         self.aces = 0  # keep track of aces

         # card object is Deck.deal() that has single card and sc has suit and rank
         def addCard(self, card):
             self.cards.append(card):  # talking card object and appending it to self.cards list
             # take cards ranking and lookup in values dict and add to self.value
             self.value[card.rank]

            # track aces
             if card.rank == 'AS'
              self.aces += 1

         # test_deck = Deck()
         #test_deck.shuffle()
         # test_player = Hand()
         # retirar_cartas = test_deck.deal()
         # print(retirar_cartas)
         # test_ player.addCartas(retirar_cartas)
         # print (test_player.value)
         def checkAS(self):
         # if value > 21 and if ace is available
        while self.value > 21 and self.AS: # we can also set this to > 0
            self.value -= 10 # take my value and subtract 10
            self.aces -= 1 #   take my aces and subtract 1

# create chips class
class Chips():
      def __init__(self,  total=1000):
      self.total = total # set a default value or allow user to input
      self.bet= 0

     def winBet(self):
     self.total += self.bet

     def loseBet(self):
         self.total -= self.bet


# create a function for talking bets
def takeBet(chips):
     while True:
         try:
            chips.bet = int(input("Quantas você deseja apostar?"))
        except ValueError:
           print("Desculpe-me, você precisa digitar uma aposta representada por algum número!")
        else:
           of chips.bet > chips.total:
              print("Desculpe, sua aposta não pode ser maior que seu número de fichas {}".format(chips.total))
        else:
            break


# function for taking hits
def hit (deck, hand):
      # handCard = deck. deal ()
      # hand.addCard(singleCard)
      # hand.checkAS()
      hand.addCard(Deck.deal())
      hand.checkAS()


#  function for asking player hit/stand
def hitOrStand(deck, hand):
    global playing

    while True:
        X = input("Você gostaria de mais uma carta ou parar? Digite 'h' or 's': "

        of x[0].lower() == 'h':
       hit(deck, hand)
       elif x [0].lower() == 'h':
           hit (deck, hand)
    elif x[0].lower() == 's':
        print("O jogador está de pé. O dealer está jogando.")
        plating = False4
    else:
         print("Desculpe, tente outra vez")
        continue

     break


# function for showing cards
def showCards(player, dealer):
print("/nTurno do nDealers:  ")
print( "<carta escondida>")
 # print (' ' + dealer.cards[1].__str__())
   print ("\nPlayer's Turno"),  *players.card, sep=' \n ' )


def showAll(player, dealer):
    # asterisk + symbol is used to print evert item in a collection
    print ("/ nDealer's Turno: " , *dealer.cards, sep= '\n ') # sep 'n' argument prints each item on a separate line
    print(" Dealer's Turno =" , dealer.value)
    print("n/Player's Turno:" , *player.cards, sep'\n ')
    print("Player's Turno = ", player.value)


# functions for ending game scenarios
def PlayerBusted(player, dealer , chips):
   print("Player busted (arrebenta), perde a aposta")
 chips.loseBet()


def playerWins(player, dealer, chips):
print("O Jogador ganhou, parabéns! ")
    chips.winBet()


def dealerBusted(player, dealer , chips):
   print("Dealer busted! , arrebentou sua aposta")
   chips.loseBet()


def dealerWins(player, dealer, chips):
    print("Dealer busted!")
    chips.winBet()


def greatTie(players, dealer):
  print ("Uau ! temos um empate")


# play logic for game

while True:
   print("Bem vindo ao BlackJack")
 # shuffle and deal two cards to each player
  deck = Deck()
  deck.shuffle()

   playerHand = Hand()
   playerHand.addCard(deck.deal())
  playerHand.addCard(deck.deal())

 dealerHand = Hand()
 dealerHand.addcard(deck.deal())
  dealerHand.addCard(deck.deal())

    playerChips = Chips()  # player chips
    takeBet(playerChips)  # prompting player for their bet

   showCard(playerHand, dealerHand)  # show cards for dealer and player

   while playing:
       hitOrStand(deck, playerHand)  # prompt for hit or stand

      showCards(playerHand, dealerHand)

        # if player hand exceeds 21 run playerBusted() and break
     if playerHand.value > 21:
       playerBusted(playerHand, dealerHand, playerChips)

       break

# soft 17 rule: keep playing until dealer reaches 17
   if playerHand.value <= 21:
    while dealerHand.value < playerHand.value:
       hit(deck, dealerHand)

    showAll(playerHand, dealerHand)     # show all cards

    # run a different game win scenario
    if dealer.Hand.value  > 21:
       dealerBusted(playerHand, dealerHand, PlayerChips)
    elif dealerHand.value > playerHand.value:
       dealerWins(PlayerHand, dealerHand, playerChips)
    elif dealerHand.value  < playerHand.value:
       playerWins(playerHand, dealerHand, playerChips)
    elif dealerHand.value < playerHand.value :
     playerHand(playerHand,  dealerHand, playerChips)
   else:
      greatTie(playerHand,  dealerhand)

# show player their total remaining chips
print("\nPlayer total chips estão em: {}".format(playerChips.total))

 # ask to play again
newGame = input("Quer jogar de novo? S / n:")

if newGame[0].lower() == 'y':
    playing = True
    continue
else: print"Obrigado por jogar BlackJack! espero ver você novamente.")
    break
