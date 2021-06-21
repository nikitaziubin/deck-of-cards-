

# print(colors)
# print(type(colors))

#print(f'0-based indexing into the list ... second item: {colors[1]}')

#print(f'Last item of the list: {colors[6]}')

#print(f'Next to last item in the list: {colors[-2]}')
#colors = ['red', 'green', 'blue']
#print(colors[2])
import random
masti = ["Hearts", "Spades", "Clubs", "Diamonds"]
number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for  suit in masti:
  for rank in number:
    deck.append(f'{rank} of {suit}')
    print(f'There are {len(deck)} cards in the deck.')
print('Dealing ...')
hand = []
while len(hand) < 5:
  card = random.choice(deck)
  deck.remove(card)
  hand.append(card)

print('Player has the following cards in their hand:')

print(f'There are {len(deck)} cards in the deck.')
print(hand)
