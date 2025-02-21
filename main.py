def main():
    # Read content from file
    with open("./books/frakenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

main()