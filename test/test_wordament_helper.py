
import pytest
import io
from py_wordament_helper.wordament_helper import wordament_helper
from py_wordament_helper.dictionary_trie import dictionary_trie


def test_solver():
    grid = 'GLNTSRAWRPHSEOPS'
    trie = dictionary_trie(["like", "shops", "shop", "wasp", "want", "hops"])
    assert(trie.number_of_words() == 6)

    helper = wordament_helper(grid, trie)
    words = helper.solve()
    assert(len(words) == 5)
    assert("shops" in words)
    assert("hops" in words)
    assert("wasp" in words)
    assert("want" in words)
    assert("hops" in words)


def test_full_dictionary():
    grid = 'GLNTSRAWRPHSEOPS'

    with(io.open("./test/words_alpha.txt")) as f:
        lines = [line.rstrip() for line in f]
        #lines = f.readlines()

    trie = dictionary_trie(lines)

    assert(trie.number_of_words() == 370103)

    helper = wordament_helper(grid, trie)
    words = helper.solve()
    assert("grasshopper" in words)
    assert("whopper" in words)
    assert("grape" in words)
    assert("warp" in words)
    assert("orphan" in words)

