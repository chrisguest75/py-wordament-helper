from typing import List, Text
from py_wordament_helper.dictionary_abc import dictionary_abc


class dictionary_trie(dictionary_abc):
    class _trie_node():
        def __init__(self, letter: Text, end_of_word: bool = False):
            """Constructs a node in the dictionary trie
            
            Arguments:
                letter {Text} -- Letter for node
            
            Keyword Arguments:
                end_of_word {bool} -- Is this letter representing the end of a word (default: {False})
            """
            self._letter = letter
            self._end_of_word = end_of_word
            self._children = {}

        def add_child(self, child):
            """Add a child to this node
            
            Arguments:
                child {[type]} -- The child to add to this node
            
            Returns:
                [type] -- The node that was added or not
            """
            if child._letter in self._children:
                node = self._children[child._letter]
                if child._end_of_word:
                    node._end_of_word = True

                return node
            else:
                self._children[child._letter] = child
                return child

        def is_child(self, letter: Text) -> bool:
            """Do we have a child with this letter?
            
            Arguments:
                letter {Text} -- The letter of child to find
            
            Returns:
                bool -- True if we have found a child node for letter
            """
            return letter in self._children

        def get_child(self, letter: Text):
            """Get the child for the letter
            
            Arguments:
                letter {Text} -- The letter of child to return
            
            Returns:
                Child -- The child node 
            """
            if letter not in self._children:
                return None
            else:
                return self._children[letter]

        def is_end_word(self) -> bool:
            """Is this the end of a word?
            
            Returns:
                bool -- True if the end of a word
            """
            return self._end_of_word

    def __init__(self, words: List = []):
        """Constructs a dictionary
        
        Keyword Arguments:
            words {List} -- A list of words to add to dictionary on construction (default: {[]})
        """
        self._num_words = 0
        self._longest_word_length = 0
        self._root_node = dictionary_trie._trie_node('*')
        self.insert_words(words)

    def number_of_words(self) -> int:
        """Number of words in the dictionary
        
        Returns:
            int -- Number of words
        """
        return self._num_words

    def longest_word_length(self) -> int:
        """Length of the longest word in the dictionary
        
        Returns:
            int -- Length of word
        """
        return self._longest_word_length

    def insert_words(self, words: List = []):
        """Insert a list of words into the dictionary
        
        Keyword Arguments:
            words {List} -- The list of words (default: {[]})
        """
        for word in words:
            if len(word) > self._longest_word_length:
                self._longest_word_length = len(word)
                
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

    def is_partial_word(self, word: Text) -> bool:
        """Is the partial word in the dictionary with children?
        NOTE: A complete word returns True
        
        Arguments:
            word {Text} -- Partial word to check for in dictionary
        
        Returns:
            bool -- True if dictionary contains word
        """
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
        if child is None and not current_node.is_end_word():
            return False
        else:
            return True

    def is_word(self, word: Text) -> bool:
        """Is the word in the dictionary
        
        Arguments:
            word {Text} -- Word to check for in dictionary
        
        Returns:
            bool -- True if dictionary contains word
        """
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

    
