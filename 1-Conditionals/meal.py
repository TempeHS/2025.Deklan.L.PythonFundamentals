def main():
    meal(input("what is the time? "))


def meal(time):
    h, m = time.split(":")
    min = float(m) / 60
    hr = float(h)
    tme = hr + min
    if tme >= 7 and tme <= 8:
        print("breakfast time")
    elif tme >= 12 and tme <= 13:
        print("lunch time")
    elif tme >= 18 and tme <= 19:
        print("dinner time")
    else:
        print("debug", tme)


main()
