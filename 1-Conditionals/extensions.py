def main():
    filetype(input("what is the name of the file? "))


def filetype(extn):
    if str(extn).endswith(".gif"):
        print("this file is an animated gif")
    elif str(extn).endswith(".jpg"):
        print("this file is a jpg image")
    elif str(extn).endswith(".jpeg"):
        print("this file is a jpeg image")
    elif str(extn).endswith(".png"):
        print("this file is a png image")
    elif str(extn).endswith(".pdf"):
        print("this file is a pdf document")
    elif str(extn).endswith(".txt"):
        print("this file is a txt text document")
    elif str(extn).endswith(".zip"):
        print("this file is a zip compressed file")
    else:
        print("application/octet-stream")


main()
