import game
import hand


class Player():
  
  def __init__(self, id, game, stack, bot):
    self.game = game
    self.stack = stack
    self.bot = bot
    self.id = id
    self.cards = []
    
  def big_blind(self):
    self.stack -= 2
    self.game.hand.pot.blind(2)
  
  def small_blind(self):
    self.stack -= 1
    self.game.hand.pot.blind(1)
    
  def dealt_card(self, card):
    self.cards.append(card)
  
  def __str__(self):
    return 'player id: ' + str(self.id) + ' stack: ' + str(self.stack) + \
    ' Cards: ' + ' '.join(map(str, self.cards))
    
    
