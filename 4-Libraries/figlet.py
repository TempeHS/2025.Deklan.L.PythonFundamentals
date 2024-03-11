from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 2:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(input("what do you want to style? ")))
