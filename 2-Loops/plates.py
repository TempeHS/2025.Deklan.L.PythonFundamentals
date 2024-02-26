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
        posval = chrval
        for i in s:
            posval = posval - 1
            alphachk = posval - 1
            if str(i).isalpha() is False:
                if str(i).isalnum() is False:
                    return False
            elif str(i).isnumeric():
                a = list(i)
                if str(s[alphachk]).isalpha():
                    return False
                elif a.index("0"):
                    return False
                else:
                    return True
            else:
                return True


main()
