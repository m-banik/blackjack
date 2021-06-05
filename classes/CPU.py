from .Player import Player
from random import randint

class CPU(Player):
  def __result_validation_handler(self):
    # if "CPU" in self.get_name():
    score = self.get_points()
    if score >= 22 or score == 21 or self.get_aces() == 2 or (score >= 15 and randint(0, 1) == 0):
      self.quit_game()
  
  def __init__(self, id):
    super().__init__(id, "CPU " + str(id), "CPU", self.__result_validation_handler)