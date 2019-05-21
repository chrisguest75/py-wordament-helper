#!/usr/bin/env python3

import io
from py_wordament_helper.wordament_helper import wordament_helper
from py_wordament_helper.dictionary_trie import dictionary_trie

if __name__ == '__main__':
    grid = 'GLNTSRAWRPHSEOPS'
    # trie = dictionary_trie(["grass", "like", "shops", "shop", "wasp", "want", "hops"])

    # Load the words from a file
    with(io.open("./test/words_alpha.txt")) as f:
        lines = [line.rstrip() for line in f]

    # Build the dictionary with one word per element in array
    trie = dictionary_trie(lines)

    assert(trie.number_of_words() == 370103)
    assert(trie.is_word("grass"))

    # Solve the grid using the dictionary
    helper = wordament_helper(grid, trie)
    words = helper.solve()
    print(words)
