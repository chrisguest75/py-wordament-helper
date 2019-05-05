
import pytest
from wordament_helper import wordament_helper
from dictionary_trie import dictionary_trie


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


