from .Player import Player

class Human(Player):
  def __handle_result_validation(self):
    name = self.get_name()
    last_card = self.get_lastly_picked_card()
    card_name = last_card.get_card_name()
    added_points = str(last_card.get_card_value())
    print()
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
      self.ask_if_continue()
    
  def ask_if_continue(self):
    name = self.get_name()
    score = str(self.get_points())
    flag = str(input("Aktualna suma zdobytych punktów wynosi " + score + ", czy " +
                     name + " chce kontynuować?[Tak/Y/Nie/N] "))
    if flag.lower() == "tak" or flag.lower() == "y":
      pass
    elif flag.lower() == "nie" or flag.lower() == "n":
      print(name + " mówi ' pas'!")
      self.quit_game()
    else:
      print("Podano nieprawidłowy format danych!")
      print()
      self.ask_if_continue()
  
  def __init__(self, id):
    super().__init__(id, "Gracz " + str(id), "Human", self.__handle_result_validation)