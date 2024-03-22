import random
import door

class CodeDoor(door.Door):
  """Represents a code door.
  Attributes:
    _correct_code (list): the correct code to open the door made of X and O
    _input (list): the user's input"""
  
  def __init__(self):
    """Randomizes the correct code."""
    self._correct_code = [random.choice(["X", "O"]) for _ in range(3)]
    self._input = [random.choice(["X", "O"]) for _ in range(3)]

  def examine_door(self):
    """Returns a string description of the code door."""
    return "You encounter a door with a coded keypad with three characters. Each key toggles a value with an ‘X’ or an ‘O’.\n"

  def menu_options(self):
    """Returns a string of the menu options that user can choose from when attempting to unlock the door."""
    return "".join(self._input) + "\n1. Press Key 1\n2. Press Key 2\n3. Press Key 3"

  def get_menu_max(self):
    """Returns the number of options in the above menu."""
    return 3

  def attempt(self, option):
    """Toggles the value of the key that the user chooses."""
    if option == 1:
      self._input[0] = "X" if self._input[0] == "O" else "O"
    elif option == 2:
      self._input[1] = "X" if self._input[1] == "O" else "O"
    elif option == 3:
      self._input[2] = "X" if self._input[2] == "O" else "O"
    return f"You press key {option}.\n"

  def is_unlocked(self):
    """Checks if the door is unlocked."""
    return self._correct_code == self._input

  def clue(self):
    """Returns a hint if the door is locked."""
    num_correct = sum(1 for i in range(3) if self._correct_code[i] == self._input[i])
    return f"You have {num_correct} correct characters in the correct positions.\n"

  def success(self):
    """Returns a congratulatory message if the door is unlocked."""
    return "You found the correct code and opened the door.\n"