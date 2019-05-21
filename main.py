#!/usr/bin/env python3

import io
from py_wordament_helper.wordament_helper import wordament_helper
from py_wordament_helper.dictionary_trie import dictionary_trie

if __name__ == '__main__':
    grid = 'GLNTSRAWRPHSEOPS'
    # trie = dictionary_trie(["grass", "like", "shops", "shop", "wasp", "want", "hops"])

    with(io.open("./test/words_alpha.txt")) as f:
        lines = [line.rstrip() for line in f]
        #lines = f.readlines()

    trie = dictionary_trie(lines)

    assert(trie.number_of_words() == 370103)
    assert(trie.is_word("grass"))

    helper = wordament_helper(grid, trie)
    words = helper.solve()
    print(words)
