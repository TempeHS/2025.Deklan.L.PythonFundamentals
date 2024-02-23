def main():
    camelcase(input())


def camelcase(txt):
    for i in txt:
        if (i).isupper():
            print("_" + i.casefold(), end="")
        else:
            print(i, end="")


main()
