import door
import random

class BasicDoor(door.Door):
  """Represents a basic door.
  Attributes:
    _state (int): the state of the door (1 for push, 2 for pull)
    _input (int): the user's input
  """
  def __init__(self):
    self._state = random.randint(1,2)
    self._input = 0

  def examine_door(self):
    return "You encounter a basic door, you can either push it or pull it to open.\n"

  def menu_options(self):
    return "1. Push\n2. Pull\n"

  def get_menu_max(self):
    return 2

  def attempt(self, option):
    self._input = option
    if self._input == 1:
      return "You push the door."
    elif self._input == 2:
      return "You pull the door."

  def is_unlocked(self):
    return self._state == self._input
    
  def clue(self):
    return "Try the other way.\n"

  def success(self):
    return "Congratulations, you opened the door.\n"