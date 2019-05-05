from abc import ABC, abstractmethod
from typing import Text


class dictionary_abc(ABC):

    @abstractmethod
    def is_word(self, word: Text) -> bool:
        """Is the word in the dictionary
        
        Arguments:
            word {Text} -- Word to check for in dictionary
        
        Returns:
            bool -- True if dictionary contains word
        """
        pass

        