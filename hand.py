import deck
import game
import player
import pot


class Hand():
  
  def __init__(self, game):
    self.game = game
    self.pot = pot.Pot(self)
    self.deck = deck.Deck()

  def play(self):
    self.game.players[self.game.small_blind].small_blind()
    if self.game.small_blind == self.game.num_players - 1: big_blind = 0
    else: big_blind = self.game.small_blind + 1
    self.game.players[big_blind].big_blind()
    for player in self.game.players:
      for i in range(2):
        player.dealt_card(self.deck.deal())
      
  
