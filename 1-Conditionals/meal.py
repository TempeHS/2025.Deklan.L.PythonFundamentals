def main():
    meal(input("what is the time? "))


def meal(time):
    h, m = time.split(":")
    min = float(m) / 60
    hrs = int(h)

    if hrs == 7:
        print("breakfast time")
    elif hrs == 8:
        if min == 0:
            print("breakfast time")
    elif hrs == 12:
        print("lunch time")
    elif hrs == 13:
        if min == 0:
            print("lunch time")
    elif hrs == 18:
        print("dinner time")
    elif hrs == 19:
        if min == 0:
            print("dinner time")
    else:
        print("nothing")


main()
