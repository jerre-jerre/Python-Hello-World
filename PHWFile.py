import PHWHelpFile

def main():
    print("hello from main")
    print("printing from context: ", repr(__name__))
    PHWHelpFile.printmethode("lol")

if __name__ == "__main__":
    main()