from typing import List, Type, Text
from dictionary_abc import dictionary_abc


class wordament_helper():
    class _board_state():
        MARK = "0"

        def __init__(self, width: int, height: int, grid: Text):
            """Construct a board state.
            
            Arguments:
                width {int} -- Width of board
                height {int} -- Height of board
                grid {Text} -- The wordsearch grid
            """
            self.width = width
            self.height = height
            self._grid = list(grid).copy()
            #print("copy " + str(self._grid))

        def copy(self):
            """Deep copy the board state
            
            Returns:
                [type] -- A copy of the state
            """
            return wordament_helper._board_state(self.width, self.height, self._grid)

        def get(self, x: int, y: int) -> Text:
            """[summary]
            
            Arguments:
                x {int} -- X position to get
                y {int} -- Y position to get
            
            """
            return self._grid[(self.width * y) + x]

        def mark(self, x: int, y: int):
            """Mark the grid to inidicate visited
            
            Arguments:
                x {int} -- X position to mark
                y {int} -- Y position to mark
            """
            self._grid[(self.width * y) + x] = self.MARK
            #print("mark " + str(self._grid))

        def check_mark(self, c: Text) -> bool:
            """Is the letter marked?
            
            Arguments:
                c {Text} -- Letter to check if marked
            
            Returns:
                [bool] -- True if marked
            """
            return self.MARK == c

    def __init__(self, grid: Text, trie: Type[dictionary_abc]):
        """Constructs the wordament_helper
        
        Arguments:
            grid {Text} -- The word square to solve
            trie {Type[dictionary_abc]} -- The dictionary supporting is_word()
        """
        self._board = wordament_helper._board_state(4, 4, grid)
        self._trie = trie

    def _solve(self, board_state, x: int, y: int, word: Text, depth: int, total_words: dict):
        """Internal method that is called recusrsively
        
        Arguments:
            board_state {[type]} -- The board state including which letters have already been visited 
            x {int} -- Current X position on board 
            y {int} -- Current Y position on board
            word {Text} -- Current word
            depth {int} -- Current depth in the board
            total_words {dict} -- Discovered words dictionary        
        """
        if not self._trie.is_partial_word(word):
            return

        if len(word) >= 3:
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
        """Use the dictionary and board to find the words in the wordament square
        
        Returns:
            List -- Words contained in the wordsquare
        """
        total_words = {}
        for y in range(0, self._board.height):
            for x in range(0, self._board.width):
                grid_state = self._board.copy()
                c = grid_state.get(x, y)
                grid_state.mark(x, y)
                self._solve(grid_state, x, y, c, 1, total_words)

        return total_words.keys()
