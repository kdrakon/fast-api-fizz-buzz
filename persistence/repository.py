import abc

from data_models.fizzbuzz import FizzBuzzAnswer


class Repository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save_fizz_buzz_answer(self, answer: FizzBuzzAnswer):
        raise NotImplementedError

