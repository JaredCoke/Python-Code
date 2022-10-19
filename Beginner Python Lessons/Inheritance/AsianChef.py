# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
from Chef import Chef

class AsianChef(Chef): #grant Asian Chef all of the recipes/functions from Chef class

    def make_special_dish(self): #this overwrites the inherited class's special dish
        print("The chef makes a special dish: orange chicken.")

    def make_fried_rice(self):
        print("The chef makes fried rice.")