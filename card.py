class Card:
  
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
    
  def __str__(self):
    return 'suit ' + self.suit + ' rank ' +  str(self.rank)
  
  
def main():
  mycard = Card(14, 'spades')
  print(mycard)
  
if __name__ == "__main__":
  main()
