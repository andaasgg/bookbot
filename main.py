file_contents = ""
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    return file_contents

def wordcount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        length = len(words)
        print(length)
    

main()
wordcount()
#print(file_contents)