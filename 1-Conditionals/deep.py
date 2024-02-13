# the great question of life, the universe and everything
mol = input("what == The meaning of life? ").lower()  # case insensitivity

# the meaning of life is only forty two or other ways to write it
if mol == "42" or mol == "forty-two" or mol == "forty two":
    print("yes")
# The meaning of life is nothing else
else:
    print("no")
