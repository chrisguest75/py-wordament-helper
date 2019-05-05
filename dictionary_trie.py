from typing import List, Text


class dictionary_trie():
    class _trie_node():
        def __init__(self, letter: Text, end_of_word: bool = False):
            self._letter = letter
            self._end_of_word = end_of_word
            self._children = {}

        def add_child(self, child):
            if child._letter in self._children:
                node = self._children[child._letter]
                if child._end_of_word:
                    node._end_of_word = True

                return node
            else:
                self._children[child._letter] = child
                return child

        def is_child(self, letter: Text) -> bool:
            return letter in self._children

        def get_child(self, letter: Text) -> bool:
            if letter not in self._children:
                return None
            else:
                return self._children[letter]

        def is_end_word(self) -> bool:
            return self._end_of_word

    def __init__(self, words: List = []):
        self._num_words = 0
        self._root_node = dictionary_trie._trie_node('*')
        self.insert_words(words)

    def number_of_words(self) -> int:
        return self._num_words

    def insert_words(self, words: List = []):
        for word in words:
            if word == "":
                continue
            word = word.lower()

            if not self.is_word(word):
                current_node = self._root_node
                for letter in word[:-1]:
                    newnode = dictionary_trie._trie_node(letter, False)
                    current_node = current_node.add_child(newnode)

                newnode = dictionary_trie._trie_node(word[len(word) - 1], True)
                current_node = current_node.add_child(newnode)
                self._num_words += 1

    def is_word(self, word: Text) -> bool:
        current_node = self._root_node
        word = word.lower()

        if word == "":
            return False

        for letter in word[:-1]:
            child = current_node.get_child(letter)
            if child is None:
                return False
            else:
                current_node = child

        child = current_node.get_child(word[len(word) - 1])
        if child is None:
            return False
        else:
            return child.is_end_word()
