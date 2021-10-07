class Text:
    def __init__(self, filename):
        if isinstance(filename, str):
            # if filename[-4::-1] == '.txt':
            fileout = open(filename, 'r')
            print("Test")
            self.text = fileout.read()
            self.len_text = len(self.text)
            self.word_num = self.sentence_num = 0
            count = 0
            for i in self.text:
                if i.isalnum():
                    count = 1
                else:
                    self.word_num = self.word_num + count
                    count = 0
                    if i == '.' or i == '?' or i == '!':
                        self.sentence_num += 1
            if count:
                self.word_num = self.word_num + count
                self.sentence_num = self.sentence_num + count
        else:
            raise TypeError("Not text file name entered.")


def main():
    string = Text("Merasmus.txt")
    print(string.text + '\n\nWord number:' + str(string.word_num) + '\n\nSentence number:' + str(string.sentence_num))


main()
