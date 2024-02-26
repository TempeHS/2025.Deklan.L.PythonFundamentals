def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    chrval = 0
    for i in s:
        chrval = chrval + 1
    if chrval > 6 or chrval < 2:
        return False
    else:
        return True


main()
