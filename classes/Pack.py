from random import randint
from .Card import Card

class Pack():
  __pack_template = [
    ["dwójka", 2],
    ["trójka", 3],
    ["czwórka", 4],
    ["piątka", 5],
    ["szóstka", 6],
    ["siódemka", 7],
    ["ósemka", 8],
    ["dziewiątka", 9],
    ["dziesiątka", 10],
    ["walet", 2],
    ["dama", 3],
    ["król", 4],
    ["as", 11],
  ]
  
  def get_pack(self):
    return self.__pack

  def get_card_by_index(self, index):
    return self.__pack[index]

  def get_pack_data(self):
    pack_data = []
    for card in self.__pack:
      pack_data.append(card.get_card_data())
    return pack_data
  
  def __init__(self):
    complete_pack = []
    for card_template in self.__pack_template:
      for _ in range(4):  
        card = Card(card_template[0], card_template[1])
        complete_pack.append(card)
    self.__pack = complete_pack

  def shuffle(self):
    shuffled_pack = []
    half = int(len(self.__pack) / 2)
    for k in range(half):
      shuffled_pack.append(self.__pack[k])
      shuffled_pack.append(self.__pack[half + k])
    self.__pack = shuffled_pack

  def shuffle_multiplied(self):
    self.shuffle()
    while randint(0, 1) == 0:
      self.shuffle()