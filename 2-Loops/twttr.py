def main():
    twt = input("wht d y wnt t twtt? ")
    for i in twt:
        if not (i).casefold() in ["a", "e", "i", "o", "u"]:
            print(i, end="")


main()
