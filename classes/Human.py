from .Player import Player

class Human(Player):
  def __result_validation_handler(self):
    name = self.get_name()
    last_card = self.get_lastly_picked_card()
    card_name = last_card.get_card_name()
    added_points = str(last_card.get_card_value())
    print(name + ", otrzymana karta w tej turze: " + card_name + " (+" + added_points + " punktów).")
    score = self.get_points()
    if score >= 22:
      print("Zdobyto " + str(score) + " punktów. " + name + " przegrywa!")
      self.quit_game()
    elif score == 21:
      print(name + " zdobywa " + str(score) + " punktów. Oczko!")
      self.quit_game()
    elif self.get_aces() == 2:
      print(name + " zdobywa dwa asy! Perskie oczko!")
      self.quit_game()
    else:
      flag = str(input("Aktualna suma zdobytych punktów wynosi " + str(score) + ", czy " +
                                            name + " chce kontynuować?[Tak/Y/Nie/N]"))
      if flag.lower() == "tak" or flag.lower() == "y":
        pass
      elif flag.lower() == "nie" or flag.lower() == "n":
        print(name + " mówi ' pas'!")
        self.quit_game()
      else:
        raise ValueError
    
  def __init__(self, id):
    super().__init__(id, "Human " + str(id), "Human", self.__result_validation_handler)