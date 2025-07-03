import card
import random

class Deck:
  
  def __init__ (self):
    self.deck = []
    suits = ['hearts', 'spades', 'diamonds', 'clubs']
    for suit in suits:
      for rank in range(2, 15):
        self.deck.append(card.Card(rank, suit))
  
  def deal(self):
    draw_position = random.randint(0, len(self.deck) - 1)
    dealt_card = self.deck[draw_position]
    self.deck.remove(dealt_card)
    return dealt_card
    
  
def main():
  mydeck = Deck()
  for i in range(52):
    print(mydeck.deal())
  assert not mydeck.deck
  
if __name__ == "__main__":
  main()
  
