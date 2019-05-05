from typing import List, Type, Text
from dictionary_abc import dictionary_abc


class wordament_helper():

    class _board_state():
        MARK = "0"

        def __init__(self, width: int, height: int, grid: Text):
            self.width = width
            self.height = height
            self._grid = list(grid).copy()
            #print("copy " + str(self._grid))

        def copy(self):
            return wordament_helper._board_state(self.width, self.height, self._grid)

        def get(self, x, y):
            return self._grid[(self.width * y) + x]

        def mark(self, x, y):
            self._grid[(self.width * y) + x] = self.MARK
            #print("mark " + str(self._grid))

        def check_mark(self, c):
            return self.MARK == c

    def __init__(self, grid: Text, trie: Type[dictionary_abc]):
        self._board = wordament_helper._board_state(4, 4, grid)
        self._trie = trie

    def _solve(self, board_state, x: int, y: int, word: Text, depth: int, total_words: dict) -> List:
        if not self._trie.is_partial_word(word):
            return

        if len(word) >= 3:
            print(f"{word} - {x} {y}")
            if self._trie.is_word(word):
                total_words[word.lower()] = True

        if depth == self._trie.longest_word_length():
            return

        grid_state = board_state.copy()
        for y_off in range(-1, 1 + 1):
            newy = y + y_off
            if newy >= 0 and newy < board_state.height:
                for x_off in range(-1, 1 + 1):
                    newx = x + x_off
                    if newx >= 0 and newx < board_state.width:
                        c = grid_state.get(newx, newy)
                        if c != grid_state.MARK:
                            new_grid_state = board_state.copy()
                            new_grid_state.mark(newx, newy)
                            self._solve(new_grid_state, newx, newy, word + c, depth + 1, total_words)
                    
    def solve(self) -> List:
        total_words = {}
        for y in range(0, self._board.height):
            for x in range(0, self._board.width):
                grid_state = self._board.copy()
                c = grid_state.get(x, y)
                grid_state.mark(x, y)
                self._solve(grid_state, x, y, c, 1, total_words)

        return total_words.keys()
