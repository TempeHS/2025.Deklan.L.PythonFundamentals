def vending_machine():
    ao = 50
    while ao > 0:
        c = int(input(f"insert cash {ao} c ").removesuffix("c"))
        if c == 25 or c == 10 or c == 5:
            if ao >= 0:
                ao = ao - c
            if ao <= 0:
                print("drink dispensed")
                break
        elif c != 25 or c != 10 or c != 5:
            print("not accepted")
            break
    while ao < 0:
        print(f"change {ao * -1} c")
        break


vending_machine()
