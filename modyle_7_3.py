class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        # self.words_dict = {}

    def get_all_words(self):
        # self.line = line
        words_dict = {}
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            with open (i, "r", encoding = "utf-8") as file:
                line = file.read().lower()
                for j in punc:
                    line = line.replace(j, "")
                words_dict[i] = line.split()
        return words_dict

    def find(self, word):
        dict = {}
        for i, g in self.get_all_words().items():
            if word.lower() in g:
                dict [i] = g.index(word.lower()) + 1
        return dict

    def count(self, word):
        dict = {}
        for i, g in self.get_all_words().items():
            if word.lower() in g:
                dict[i] = g.count(word.lower())
                # dict.update({self.file_names: g + 1})
        return dict




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего