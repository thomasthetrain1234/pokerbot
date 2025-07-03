import player
import bot
import hand


class Game():
  
  def __init__(self, num_players, stack):
    self.players = []
    self.num_players = num_players
    for i in range(0, self.num_players):
      self.players.append(player.Player(i, self, stack, bot.Bot()))
    self.small_blind = 0
  
  def new_hand(self):
    self.hand = hand.Hand(self)
    self.hand.play()
    
    # last thing
    #if self.big_blind = num_players - 1: self.big_blind = 0
    #else: self.big_blind += 1

  def __str__(self):
    return '\n'.join(map(str, self.players))
      

def main():
  game = Game(5, 160)
  game.new_hand()
  print(game)
  
if __name__ == "__main__":
  main()
