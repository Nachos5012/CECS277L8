# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 03/21/2024
# Module 8 - Escape Room
# Purpose - create an excape room with three doors that have different methods to opening them

# imports
import basicdoor
import codedoor
import combodoor
import deadboltdoor
import lockeddoor
import check_input
import random

def open_door(door):
  """Function to open the door.
  Examines the door and displays the menu options.
  Get the user's input and attempt to open the door.
  If the door is unlocked, display a success message.
  If the door is locked, display a clue and return to the menu.
  """
  print(door.examine_door())
  print(door.menu_options())
  option = check_input.get_int_range("Enter choice: ", 1, door.get_menu_max())
  print(door.attempt(option))
  while not door.is_unlocked():
    print(door.clue())
    print(door.menu_options())
    option = check_input.get_int_range("Enter choice: ", 1, door.get_menu_max())
    print(door.attempt(option))
  print(door.success())

def main():
  """Main function to run the escape room."""
  print("Welcome to the Escape Room. You must unlock 3 doors to escape...\n")
  doors = [basicdoor.BasicDoor(), codedoor.CodeDoor(), combodoor.ComboDoor(), deadboltdoor.DeadboltDoor(), lockeddoor.LockedDoor()]
  random.shuffle(doors)
  for i in range(3):
    open_door(doors[i])
  print("Congratulations! You escaped... this time.")

main()