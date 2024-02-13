def main():
    # can be made simpler but this is laid out better
    greeting(input("The teller answers "))


def greeting(ans):
    if "hello" in ans:  # detect if hello is said
        print("$0")
    elif str(ans).startswith("h"):  # detect if greeting starts with h
        print("$20")
    else:  # you did it
        print("$100")


main()
