def main():
    solve(input("= "))


def solve(exp):
    x, y, z = exp.split(" ")
    if y == "/" or y == "%":
        print(float(x) / float(z))
    elif y == "x" or y == "*":
        print(float(x) * float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "+":
        print(float(x) + float(z))
    else:
        print("error")


main()
