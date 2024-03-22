import abc

class Door(abc.ABC):
  """Represents a door.
  Functions:
  examine_door() - returns a string description of the door.
  menu_options() - returns a string of the menu options that user can choose from when attempting to unlock the door
  get_menu_max() - returns the number of options in the above menu.
  attempt(option) - passes in the user's selection. Returns a string describing what the user attempted.
  is_unlocked() - returns True if the door is unlocked, False otherwise.
  clue() - returns a string that gives the user a clue to help them unlock the door.
  success() - returns a string congratulating the user on opening the door.
  """
  @abc.abstractmethod
  def examine_door(self):
    pass

  @abc.abstractmethod
  def menu_options(self):
    pass

  @abc.abstractmethod
  def get_menu_max(self):
    pass

  @abc.abstractmethod
  def attempt(self, option):
    pass

  @abc.abstractmethod
  def is_unlocked(self):
    pass

  @abc.abstractmethod
  def clue(self):
    pass

  @abc.abstractmethod
  def success(self):
    pass