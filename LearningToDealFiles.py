def main():
    f = open("textfile.txt","w+")

    for i in range(10):
        f.write("This is line : " + str(i+1) + "\n")
    f.close()

    f = open("textfile.txt", "a")

    for i in range(10):
        f.write("This is line appended : " + str(i + 1) + "\n")
    f.close()

    f = open("textfile.txt","r")
    if f.mode == "r":
        contents = f.read()
        print(contents)
    f.close()

    print('Using Readlines ..... ')

    f = open("textfile.txt","r")
    if f.mode == "r":
        fl = f.readlines()
        for x in fl:
            print(x)
    f.close()


if __name__ == "__main__":
    main()