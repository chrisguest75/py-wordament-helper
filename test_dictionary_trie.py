import pytest
from dictionary_trie import dictionary_trie


def test_empty():
    trie = dictionary_trie([])
    assert(trie.number_of_words() == 0)


def test_initialise_with_words():
    trie = dictionary_trie(["word1", "word2", "spare"])
    assert(trie.number_of_words() == 3)


def test_initialise_with_empty_words():
    trie = dictionary_trie(["", "word2", ""])
    assert(trie.number_of_words() == 1)


def test_insert_words():
    trie = dictionary_trie(["word1", "word2", "spare"])
    trie.insert_words(["word3"])
    assert(trie.number_of_words() == 4)

    trie.insert_words(["word4"])
    assert(trie.number_of_words() == 5)


def test_is_word():
    trie = dictionary_trie(["word1", "word2", "spare", "bus"])
    assert(trie.is_word("word1"))
    assert(trie.is_word("bus"))
    assert(trie.is_word("spare"))
    assert(not trie.is_word("word3"))
    assert(not trie.is_word("buss"))


def test_not_word_if_empty():
    trie = dictionary_trie(["word1", "word2"])
    assert(not trie.is_word(""))


def test_words_are_lower_case():
    trie = dictionary_trie(["word1", "word2"])
    assert(trie.number_of_words() == 2)
    trie.insert_words(["Word3"])
    assert(trie.number_of_words() == 3)
    assert(trie.is_word("word3"))
    assert(trie.is_word("Word3"))


def test_insert_same_word():
    trie = dictionary_trie(["word1", "word2"])
    trie.insert_words(["word3"])
    assert(trie.number_of_words() == 3)
    trie.insert_words(["word3"])
    assert(trie.number_of_words() == 3)
    trie.insert_words(["word1"])
    assert(trie.number_of_words() == 3)


def test_overlapping_words():
    trie = dictionary_trie(["wordament", "word", "work", "top"])
    assert(trie.number_of_words() == 4)
    assert(trie.is_word("word"))
    assert(trie.is_word("work"))
    assert(trie.is_word("top"))
    assert(trie.is_word("wordament"))


#def test_get_possible_next_letters():
#    trie = dictionary_trie(["wordament", "word", "work"])
#    assert(trie.get_possible_next_letters("wor") == ['k', 'd'])

