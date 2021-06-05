class Player():
  def get_id(self):
    return self.__id
  
  def get_name(self):
    return self.__name
  
  def get_type(self):
    return self.__type
  
  def get_points(self):
    return self.__points
  
  def get_cards(self):
    return self.__cards
  
  def get_card_by_index(self, index):
    return self.__cards[index]
  
  def get_lastly_picked_card(self):
    index = len(self.__cards) - 1
    return self.get_card_by_index(index)
  
  def get_aces(self):
    return self.__aces
  
  def get_is_playing(self):
    return self.__isPlaying
  
  def print_complete_data(self):
    print(self.__id)
    print(self.__name)
    print(self.__type)
    print(str(self.__points))
    print(str(self.__aces))
    print(str(self.__isPlaying))
    for card in self.__cards:
      print(card.get_card_data())
  
  def add_card(self, card):
    self.__cards.append(card)
    self.__points += card.get_card_value()
    if card.get_card_name() == "as":
      self.__aces += 1
    self.__validate_result()
    
  def quit_game(self):
    self.__isPlaying = False
  
  def __init__(self, id, name, type, result_validation_handler):
    self.__id = id
    self.__name = name
    self.__type = type
    self.__points = 0
    self.__aces = 0
    self.__isPlaying = True
    self.__cards = []
    self.__validate_result = result_validation_handler