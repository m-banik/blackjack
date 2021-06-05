class Card():
  def get_card_name(self):
    return self.__name
    
  def get_card_value(self):
    return self.__value
  
  def get_card_data(self):
    return [self.__name, self.__value]
  
  def __init__(self, name, value):
    self.__name = name
    self.__value = value