def main():
    grocerylist()


def grocerylist():
    groceries = []
    while True:
        try:
            item = input()
            groceries = groceries + [(item, 1)]
        except EOFError:
            print(groceries)
            break


main()
