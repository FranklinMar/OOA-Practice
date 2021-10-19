import os


class Text:
    """
    Instance of Class contains path to the file and has methods required for a work with text file.
    Constructor checks if given path exists and tries to open and close it.
    Methods 'num_...' return number of objects in text file, such as:
    characters, words, lines and sentences.
    (Method 'num_characters' returns number of characters in file.
    Method 'num_lines' returns number of lines in file.
    Method 'num_words' returns number of words in file.
    Method 'num_sentences' returns number of sentences in file.)
    """
    def __init__(self, filename):
        if not isinstance(filename, str):
            raise TypeError("Not a path string entered.")
        if not os.path.isfile(filename):
            raise OSError(f"Path to the file '{filename}' does not exist.")
        fileout = open(filename, 'r')
        fileout.close()
        self.filename = filename

    def num_characters(self):
        out = open(self.filename)
        text = "".join(out.readlines())
        length = len(text)
        out.close()
        return length

    def num_lines(self):
        out = open(self.filename)
        text = out.readlines()
        out.close()
        return len(text)

    def num_words(self):
        out = open(self.filename)
        text = "".join(out.readlines())
        word_num = count = 0
        out.close()
        for i in text:
            if i.isalnum():
                count = 1
            else:
                word_num = word_num + count
                count = 0
        if count:
            word_num = word_num + count
        return word_num

    def num_sentences(self):
        out = open(self.filename)
        text = "".join(out.readlines())
        out.close()
        text = text.replace('!', '.')
        text = text.replace('?', '.')
        return len(text.rsplit('.')) - 1


def main():
    string = Text("Merasmus.txt")
    print(f'\n\nText len:{string.num_characters()}\nWord number:{string.num_words()}',
          f'\nSentence number:{string.num_sentences()}\nLines number:{string.num_lines()}')


main()
