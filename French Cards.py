# French Cards

# French Cards have two states: hidden and visible.
# Choose 1 or 2 to flip that card between hidden and visible.
# Every time you hide a card, it's replaced with a
# random card from the rest of the deck.
# Game is over when all cards have been shown and then hidden.


import random


# hidden and deck used as constants.

hidden = True

# All cards encoded into a list
deck = list(range(100,113)) + \
       list(range(200,213)) + \
       list(range(300,313)) + \
       list(range(400,413))


def printcards (card1, cardstate1, card2, cardstate2):
    rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suit = ["0", "Hearts", "Spades", "Diamonds", "Clubs"]

    # Translate each deck code to a card to output
    if card1:
        cardrank = card1%100
        cardsuit = card1//100
        cardtoprint1 = rank[cardrank] + " of " + suit[cardsuit] 
    else:
        cardtoprint1 = "<     >" # No cards left to play here.

    if card2:
        cardrank = card2%100
        cardsuit = card2//100
        cardtoprint2 = rank[cardrank] + " of " + suit[cardsuit] 
    else:
        cardtoprint2 = "<     >"
        
    if card1 and cardstate1 == hidden:
        cardtoprint1 = "<==1==>" # Card is face down
    if card2 and cardstate2 == hidden:
        cardtoprint2 = "<==2==>"

    print ("\n", cardtoprint1, "   ", cardtoprint2, "\n")
    return None


# picks a random card from the deck after removing the current card.
def setcard (excludelist):
    for card in excludelist:
        if card in deck:
            deck.remove (card)
    if deck:
        card = random.choice (deck)
    else:
        card = False
    return card


def main ():
    cardstate1 = cardstate2 = hidden
    card1 = card2 = 0
    excludelist = [card1, card2]
    card1 = setcard (excludelist)
    card2 = setcard (excludelist)

    while card1 or card2:
        excludelist = [card1, card2]
        printcards (card1, cardstate1, card2, cardstate2)
        click = input ("Click a card (enter 1 or 2): ")
        if click == '1' and cardstate1 == hidden:
            cardstate1 = not hidden
        elif click == '1' and cardstate1 == (not hidden):
            cardstate1 = hidden
            card1 = setcard (excludelist)
        elif click == '2' and cardstate2 == hidden:
            cardstate2 = not hidden
        elif click == '2' and cardstate2 == (not hidden):
            cardstate2 = hidden
            card2 = setcard (excludelist)
        else: # any other input quits.
            break

    if not deck:
        printcards (card1, cardstate1, card2, cardstate2)
        print ("All cards played.")
    else:
        print ("\nQuitting.")
        
    return None


##

main ()

##
