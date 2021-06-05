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
      print("")
      flag = str(input("Czy chce Pan/i grać dalej?[Tak/Y/Nie/N]"))
      if flag.lower() == "tak" or flag.lower() == "y":
        print("")
        self.start_game()
      elif flag.lower() == "nie" or flag.lower() == "n":
        pass
      else:
        raise ValueError
    except ValueError:
      print("Podano nieprawidłowy format danych.")
  
  def start_game_loop(self):
      while self.__players.get_current_players_number() > 0:
        pack = self.__pack.shuffle_multiplied()
        for player in self.__players.get_players():
          if player.get_is_playing():
            picked_card = self.__pack.get_pack().pop(0)
            player.add_card(picked_card)
            # player.print_complete_data()
      self.__players.set_current_players_number()
      print(self.__players.get_current_players_number())
  
  # def check_results(self):
        #     winnable_players = []
        # with_aces = []
        # # Przerwa i wydruk punktacji wszystkich graczy.
        # print()
        # print("Punktacja:")
        # for player in players:
        #     notification = player[0] + ", " + str(player[1]) + " punktów, w tym " + str(player[3]) + " as/-y/-ów."
        #     if player[3] == 2:
        #         notification += " Perskie oczko!"
        #         with_aces.append(player)
        #     elif player[1] <= 21:
        #         winnable_players.append(player)
        #     print(notification)

        # # Rozstrzygnięcie. Remis oznacza wygraną banku.
        # if len(with_aces) > 1:
        #     print("Więcej niż jedno perskie oczko! Wygrywa bank!")
        # elif len(with_aces) == 1:
        #     print(with_aces[0][0] + " wygrywa!")
        #     # Rozpoznanie czy wygrał człowiek, czy maszyna. Dalej inne przypadki.
        #     if "CPU" in with_aces[0]:
        #         print("Brawa dla komputera!")
        #     else:
        #         print("Brawa dla gracza!")
        # else:
        #     n = len(winnable_players)
        #     while n > 1:
        #         altered = False
        #         for i in range(len(winnable_players) - 1):
        #             if winnable_players[i][1] > winnable_players[i + 1][1]:
        #                 winnable_players[i], winnable_players[i + 1] = winnable_players[i + 1], winnable_players[i]
        #                 altered = True
        #         if not altered:
        #             break
        #     print()

        #     if n == 0 or (n > 1 and winnable_players[n - 1][1] == winnable_players[n - 2][1]):
        #         print("Remis! Wygrywa bank!")
        #     else:
        #         winner = winnable_players[n - 1]
        #         notification = winner[0] + " wygrywa!"
        #         if winner[1] == 21:
        #             notification += " Oczko! :)"
        #         print(notification)
        #         if "CPU" in winner[0]:
        #             print("Brawa dla komputera!")
        #         else:
        #             print("Brawa dla gracza!")
        # # Zapytanie gracza/graczy, czy chcą kontynuować.
        # print("")
        # flag = str(input("Czy chce Pan/i grać dalej?[Tak/Y/Nie/N]"))
        # if flag.lower() == "tak" or flag.lower() == "y":
        #     print("")
        #     play_game()
        # elif flag.lower() == "nie" or flag.lower() == "n":
        #     pass
        # else:
        #     raise ValueError
      