import csv
from library import menu


with open("menu.csv", "r") as file:
    for line in file:
        print(line)

