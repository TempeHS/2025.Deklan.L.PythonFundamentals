import inflect

p = inflect.engine()


def main():
    namelist = []
    while True:
        try:
            name = input("names= ")
            namelist.append(name)
        except EOFError:
            goodbye(namelist)
            break


def goodbye(people):
    frmtname = p.join(people)
    print("\nAdieu, adieu, to", frmtname)


main()
