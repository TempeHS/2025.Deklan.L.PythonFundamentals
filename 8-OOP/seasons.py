from datetime import date


class Minutes:

    def main():
        birthday = get_birthday()


def get_birthday():
    birthday = input("What is your birthday?(format in YYYY-MM-DD): ")
    year = str(birthday).split("-")
    print(year)


if __name__ == "__main__":
    main()
