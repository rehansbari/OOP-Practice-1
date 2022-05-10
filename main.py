import turtle
from turtle import Turtle, Screen
import prettytable

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = prettytable.PrettyTable()

table.add_column("Pokemon",
                 ["Pikachu", "Squirtle"])
table.add_column("Type",
                 ["Lightning", "Water"])
table.align = "l"
print(table)