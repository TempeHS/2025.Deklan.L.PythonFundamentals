from pyfiglet import Figlet
import sys
import random


def main():
    if len(sys.argv) >= 3 and len(sys.argv) <= 3:
        manualfont(input("what do you want to style? "))
    elif len(sys.argv) < 1:
        randomfont(input("what do you want to style? "))
    else:
        sys.exit
        print("invalid usage")


def manualfont(txt):
    figlet = Figlet()
    if str(sys.argv[1]) == "-f" or str(sys.argv[1]) == "--font":
        if sys.argv[2] in figlet.getFonts():
            f = Figlet(font=sys.argv[2])
            print(f.renderText(txt))
        else:
            sys.exit
            print("invalid usage")
    else:
        sys.exit
        print("invalid usage")


def randomfont(txt):
    figlet = Figlet()
    fntlst = figlet.getFonts()
    f = Figlet(random.choice(fntlst))
    print(f.renderText(txt))


main()
