def main():
    print(camelcase(input()))


def camelcase(txt):
    for i in txt:
        if (i).isupper():
            r = "_" + i
            str(txt).replace(i, r)
            return txt


main()
