def main():
    n = fract(input("how much fuel do you have left? "))
    print(str(n) + "%")


def fract(n):
    while True:
        try:
            percent = n.split("/")
            x, y = percent[0], percent[1]
            percent = int(x) / int(y) * 100
            if percent <= 1:
                print("E")
                break
            elif percent >= 99 and percent < 101:
                print("F")
                break
            elif percent > 100:
                pass
            else:
                return percent
        except ValueError:
            print("improper value")
            pass
        except ZeroDivisionError:
            print("denominator must not be zero")
            pass


main()
