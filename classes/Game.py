from .Players import Players
from .Pack import Pack

class Game():
  def __init__(self):
    self.start_game()
    
  def start_game(self):
    self.__players = Players()
    self.__pack = Pack()
    self.__pack.shuffle_multiplied()
    self.start_game_loop()
    
  def ask_if_repeat(self):
    try:
      print()
      flag = str(input("Czy chce Pan/i grać dalej?[Tak/Y/Nie/N] "))
      if flag.lower() == "tak" or flag.lower() == "y":
        self.start_game()
      elif flag.lower() == "nie" or flag.lower() == "n":
        print("Dziękujemy za grę. :)")
      else:
        raise ValueError
    except ValueError:
      print("Podano nieprawidłowy format danych!")
      return self.ask_if_repeat()
  
  def start_game_loop(self):
    while self.__players.get_current_players_number() > 0:
      pack = self.__pack.shuffle_multiplied()
      for player in self.__players.get_players():
        if player.get_is_playing():
          picked_card = self.__pack.get_pack().pop(0)
          player.add_card(picked_card)
      self.__players.set_current_players_number()
    self.check_results()
  
  def check_results(self):
    winnable_players = []
    with_aces = []
    print()
    print("Punktacja:")
    for player in self.__players.get_players():
      name = player.get_name()
      score = player.get_points()
      aces_number = player.get_aces()
      notification = name + ", " + str(score) + " punktów, w tym " + str(aces_number) + " as/-y/-ów."
      if aces_number >= 2:
        notification += " Perskie oczko!"
        with_aces.append(player)
      elif score <= 21:
        winnable_players.append(player)
      print(notification)

    if len(with_aces) > 1:
      print("Więcej niż jedno perskie oczko! Wygrywa bank!")
    elif len(with_aces) == 1:
      print(with_aces[0].get_name() + " wygrywa!")
      if "CPU" == with_aces[0].get_type():
        print("Brawa dla komputera!")
      else:
        print("Brawa dla gracza!")
    else:
      n = len(winnable_players)
      while n > 1:
        altered = False
        for i in range(len(winnable_players) - 1):
          if winnable_players[i].get_points() > winnable_players[i + 1].get_points():
            winnable_players[i], winnable_players[i + 1] = winnable_players[i + 1], winnable_players[i]
            altered = True
        if not altered:
          break
      print()
      if n == 0 or (n > 1 and winnable_players[n - 1].get_points() == winnable_players[n - 2].get_points()):
        print("Remis! Wygrywa bank!")
      else:
        winner = winnable_players[n - 1]
        notification = winner.get_name() + " wygrywa!"
        if winner.get_points() == 21:
          notification += " Oczko! :)"
        print(notification)
        if "CPU" == winner.get_type():
          print("Brawa dla komputera!")
        else:
          print("Brawa dla gracza!")
    self.ask_if_repeat()      