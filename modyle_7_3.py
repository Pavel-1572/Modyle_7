
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.words_dict = {}

    def get_all_words(self, line):
        self.line = line
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        line = line.lower()
        for i in line:
            if i in punc:
                line = i + line
        for file_name in self.file_names:
            with open(file_name, 'r') as file:
                words = file.read().split()
                self.words_dict[file_name] = words
        return self.words_dict

    def find(self, word):
        dist = {}
        world = self.get_all_words()[self.file_names]
        for i in range(len(world)):
            if txt.lower() == world[i]:
                dist.update({self.file_names: i + 1})
                return dist



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

