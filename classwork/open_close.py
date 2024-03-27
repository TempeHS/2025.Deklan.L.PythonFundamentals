with open("myText.txt", "r") as file:
    number = int(file.readline()[3])

with open("myText.txt", "w") as file:
    file.write(str(number + 1))
    file.close
