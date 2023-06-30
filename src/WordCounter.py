class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence

    def count_words(self):
        word_count = len(self.sentence.split())
        return word_count

    def get_word_count(self):
        return self.count_words()

    def get_shortest_word(self):
        words = self.sentence.split()
        shortest_word = min(words, key=len)
        return len(shortest_word)

    def get_longest_word(self):
        words = self.sentence.split()
        longest_word = max(words, key=len)
        return len(longest_word)

