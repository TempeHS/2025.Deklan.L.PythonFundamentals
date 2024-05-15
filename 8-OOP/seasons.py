import datetime


class Minutes:
    def __init__(self, bd):
        year = int(bd[0])
        month = int(bd[1])
        day = int(bd[2])
        self.year = year
        self.month = month
        self.day = day

    def __self__(self):
        return f"{self.today - self.bdate}"

    def to_min(self, year, month, day):
        year = year * 525600

    def date_def(self, bdate, today):
        if self.bdate:
            return datetime.date(self.year, self.month, self.day)
        elif self.today:
            return datetime.date.today()


def main():
    get_birthday()
    date_difference()


def get_birthday():
    birthday = input("What is your birthday?(format in YYYY-MM-DD): ")
    bd = str(birthday).split("-")
    return Minutes(bd)


def date_difference():
    bdate = Minutes.date_def
    today = Minutes.date_def
    diff = today - bdate
    print(diff)


if __name__ == "__main__":
    main()
