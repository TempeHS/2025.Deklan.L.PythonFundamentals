def main():
    dollars = d_float(input("How much was the meal? "))  # ask for val
    percent = p_float(input("What % would you like to tip? "))  # ask for val
    tip = float(dollars * percent)  # find tip val
    print(f"Leave ${tip:.2f}")  # format tip val


def d_float(d):
    d = float((d).removeprefix("$"))  # remove dollar sign then conv float
    return d  # return val


def p_float(p):
    p = (
        float((p).removesuffix("%")) / 100
    )  # remove percent then conv float and div by 100
    return p  # return val


main()
