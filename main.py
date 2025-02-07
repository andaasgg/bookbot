from collections import Counter
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

def charcount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_string = file_contents.lower()
        char_count = Counter(lowered_string)
        print(char_count)

#main()
#wordcount()
charcount()
#print(file_contents)