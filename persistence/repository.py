import abc

from data_models.fizzbuzz import FizzBuzzAnswer


class Repository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def save_fizz_buzz_answer(self, key: str, answer: FizzBuzzAnswer):
        raise NotImplementedError

