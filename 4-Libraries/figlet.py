from pyfiglet import Figlet
import sys
from random import choice


def main():
    if len(sys.argv) >= 2:
        manualfont(input("what do you want to style? "))
    if len(sys.argv) <= 1:
        randomfont(input("what do you want to style? "))


def manualfont(txt):
    if str(sys.argv[1]) == "-f":
        f = Figlet(font=sys.argv[2])
        print(f.renderText(txt))


def randomfont(txt):
    figlet = Figlet()
    f = choice([figlet.getFonts()])
    print(f.renderText(txt))


main()
