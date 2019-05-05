from abc import ABC, abstractmethod
from typing import Text


class dictionary_abc(ABC):

    @abstractmethod
    def is_word(self, word: Text) -> bool:
        pass

        