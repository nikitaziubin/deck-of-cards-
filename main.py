class Participant:
  def __init__(self, name):
    self.name = name
    self.points = 0
    self.choice = ""
  def choose(self):
    self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
    print("{name} selects {choice}".format(name=self.name, choice = self.choice))

class GameRound:
  def __init__(self, p1, p2):
    p1.choose()
    p2.choose()
  def compareChoices(self, p1, p2):
    if p1.choice == "rock" and p2.choice == "scissor":
      return 1
    elif p1.choice == "paper" and p2.choice == "rock":
      return 1
    elif p1.choice == "scissor" and p2.choice == "paper":
      return 1
    elif p1.choice == "paper" and p2.choice == "scissor":
      return -1
    elif p1.choice == "scissor" and p2.choice == "rock":
      return -1
    elif p1.choice == "rock" and p2.choice == "paper":
      return -1
    elif p1.choice == "scissor" and p2.choice == "scissor":
      return 0
    elif p1.choice == "rock" and p2.choice == "rock":
      return 0
    elif p1.choice == "scissor" and p2.choice == "scissor":
      return 0
    else:
        return 0
    
  def awardPoints(self):
    print("implement")

class Game:
  def __init__(self):
    self.endGame = False
    self.participant = Participant("Spock")
    self.secondParticipant = Participant("Kirk")
  def determineWinner(self):
    resultString = "It's a Draw"
    if self.participant.points > self.secondParticipant.points:
        resultString = "Winner is {name}".format(name=self.participant.name)
    elif self.participant.points < self.secondParticipant.points:
        resultString = "Winner is {name}".format(name=self.secondParticipant.name)
    print(resultString)
  def checkEndCondition(self):
    answer = input("Continue game y/n:")
    if answer == 'y':
      game_round = GameRound(self.participant, self.secondParticipant)
      result = game_round.compareChoices(self.participant, self.secondParticipant)
      if result == 1:
        self.participant.points += 1
        self.checkEndCondition()
        print('Spock win')
      elif result == -1:
        self.secondParticipant.points += 1
        self.checkEndCondition()
        print('kirk win')
      else:
        self.checkEndCondition()
        print('ничья')
    
    else:
      print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
      self.determineWinner()
      self.endGame = True  
  def start(self):
    while not self.endGame:      
        self.checkEndCondition()
      
      
    
  def determineWinner(self):
   print("")
game = Game()
game.start()
