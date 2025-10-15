from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def can_handle(seld, update: dict) -> bool: ...

    @abstractmethod
    def handle(seld, update: dict) -> bool:
        """
        return options:
        - true - signal for dispatcher to continue processing
        - false - signal for dispatcher to STOP processing
        """
        pass