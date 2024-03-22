import random
import door


class LockedDoor(door.Door):
  """Represents a locked door.
  Attributes:
    key_location (int): location of the key
    input (int): user's input
  """

  def __init__(self):
    """Randomizes the location of the key."""
    self._key_location = random.randint(1, 3)
    self._input = 0

  def examine_door(self):
    """Returns a string description of the locked door."""
    return "You encounter a locked door. Look around for the key.\n"

  def menu_options(self):
    """Returns a string of the menu options that user can choose from when attempting to unlock the door."""
    return "1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock.\n"

  def get_menu_max(self):
    """Returns the number of options in the above menu."""
    return 3

  def attempt(self, option):
    self._input = option
    if option == 1:
      return "You look under the mat."
    if option == 2:
      return "You look under the flower pot."
    if option == 3:
      return "You look under the fake rock."

  def is_unlocked(self):
    return self._input == self._key_location

  def clue(self):
    return "Look somewhere else.\n"

  def success(self):
    return "Congratulations, you found the key and opened the door.\n"
