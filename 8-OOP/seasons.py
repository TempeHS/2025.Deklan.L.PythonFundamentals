from datetime import date


class Minutes:
    def __init__(self, year, month, day):
        date(year, month, day)


def main():
    birthday = get_birthday()
    print(date.today())


def get_birthday():
    birthday = input("What is your birthday?(format in YYYY-MM-DD): ")
    bd = str(birthday).split("-")
    year = int(bd[0])
    month = int(bd[1])
    day = int(bd[2])
    return Minutes(year, month, day)


if __name__ == "__main__":
    main()
