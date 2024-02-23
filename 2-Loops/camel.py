def main():
    camelcase(input())


def camelcase(txt):
    for i in txt:
        if (i).isupper():
            r = str(txt).replace(i, "_" + str(i).casefold())
            if (r).isupper():
                break
        for j in txt:
            if (j).isupper():
                s = str(r).replace(j, "_" + str(j).casefold())
                print(s)


main()
