import random
import door

class DeadboltDoor(door.Door):
  """Represents a deadbolt door.
  Attributes:
    bolt1 (bool): first bolt
    bolt2 (bool): second bolt
  """
  
  def __init__(self):
    """Randomizes the state of the two bolts."""
    self._bolt1 = random.choice([True, False])
    self._bolt2 = random.choice([True, False])

  def examine_door(self):
    """Returns a string description of the deadbolt door."""
    return "You encounter a double deadbolt door, both deadbolts must be unlocked to open it, but you can't tell from looking at them whether they're locked or unlocked.\n"

  def menu_options(self):
    """Returns a string of the menu options that user can choose from when attempting to unlock the door."""
    return "1. Toggle bolt 1\n2. Toggle bolt 2\n"

  def get_menu_max(self):
    """Returns the number of options in the above menu."""
    return 2

  def attempt(self, option):
    if option == 1:
      self._bolt1 = not self._bolt1
      return "You toggle the first bolt."
    elif option == 2:
      self._bolt2 = not self._bolt2
      return "You toggle the second bolt."

  def is_unlocked(self):
    return self._bolt1 and self._bolt2

  def clue(self):
    if (self._bolt1 and not self._bolt2) or (not self._bolt1 and self._bolt2):
      return "You jiggle the door... it seems like one of the bolts is unlocked.\n"
    elif (not self._bolt1 and not self._bolt2):
      return "You jiggle the door... it seems like it's completely locked.\n"

  def success(self):
    return "You unlocked both deadbolts and opened the door\n"