import random
import door

class ComboDoor(door.Door):
  """Represents a combination door.
  Attributes:
    _correct_value (int): the correct value to open the door (1-10)
    _input (int): the user's input
  """
  def __init__(self):
    """Randomizes the correct value."""
    self._correct_value = random.randint(1,10)
    self._input = 0

  def examine_door(self):
    """Returns a string description of the combination door."""
    return "You encounter a door with a combination lock, you can spin the dial to a number 1-10.\n"

  def menu_options(self):
    """Returns a string of the menu options that user can choose from when attempting to unlock the door."""
    return "Enter a number 1-10: "

  def get_menu_max(self):
    """Returns the number of options in the above menu."""
    return 10

  def attempt(self, option):
    self._input = option
    return "You turn the dial to... " + str(option)

  def is_unlocked(self):
    return self._correct_value == self._input

  def clue(self):
    if self._input > self._correct_value:
      return "Try a lower value.\n"
    elif self._input < self._correct_value:
      return "Try a higher value.\n"

  def success(self):
    return "You found the correct value and opened the door.\n"