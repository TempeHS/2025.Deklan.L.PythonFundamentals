from pyfiglet import Figlet
import sys


def main():
    if len(sys.argv) == 2:
        print(manualfont)


def manualfont():
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
        Figlet.setFont(font=f)
        unstyledtext = input("what do you want to style? ")
        print(f.renderText(unstyledtext))


main()
