from abc import ABC, abstractmethod


class Middleware(ABC):
    '''Base class for Pbot Middleware.'''

    @abstractmethod
    def handle_messages(self, messages: list[dict]) -> list[dict]:
        '''Abstract method to override with your own.

        Args:
            messages (list[dict]): A list of messages dictionaries.

        Returns:
            list[dict]: A list of messages dictionaries.
        '''
        raise NotImplementedError

        return messages
