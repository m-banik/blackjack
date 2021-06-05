from .Human import Human
from .CPU import CPU

class Players():
  def __init__(self):
    self.__players = []
    self.create_players()
    self.__current_players_number = len(self.__players)
  
  def get_current_players_number(self):
    return self.__current_players_number
  
  def get_players(self):
    return self.__players
  
  def create_players(self):
    try:
      players_number = int(input("Proszę podać ilość graczy: "))
      if players_number < 2 or players_number > 4:
        raise ValueError
      cpus_number = int(input("Proszę podać ilość graczy sterowanych przez komputer: "))
      if cpus_number < 0 or (players_number - cpus_number < 1) or ((players_number - 1) < cpus_number):
        raise ValueError
    except ValueError:
      print("Graczy może być tylko 2 - 4, z czego przynajmniej jeden musi być człowiekiem!")
    for i in range(1, cpus_number + 1):
      self.__players.append(CPU(i))
    for i in range(1, players_number - cpus_number + 1):
      self.__players.append(Human(i))
  
  def set_current_players_number(self):
    current_players_number = 0
    for player in self.__players:
      if player.get_is_playing():
        current_players_number += 1
    self.__current_players_number = current_players_number
