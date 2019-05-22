#!/usr/bin/env python3

import io
import logging
from py_wordament_helper.wordament_helper import wordament_helper
from py_wordament_helper.dictionary_trie import dictionary_trie

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    grid = 'GLNTSRAWRPHSEOPS'
    # trie = dictionary_trie(["grass", "like", "shops", "shop", "wasp", "want", "hops"])
    logging.info(f"grid = {grid}")

    # Load the words from a file
    with(io.open("../test/words_alpha.txt")) as f:
        lines = [line.rstrip() for line in f]

    # Build the dictionary with one word per element in array
    logging.info(f"word count = {len(lines)}")

    trie = dictionary_trie(lines)

    assert(trie.number_of_words() == len(lines))
    logging.info(f"trie word count = {trie.number_of_words()}")

    assert(trie.is_word(lines[1000]))

    # Solve the grid using the dictionary
    helper = wordament_helper(grid, trie)
    words = helper.solve()
    logging.info(words)
