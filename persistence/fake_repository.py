from data_models.fizzbuzz import FizzBuzzAnswer
from persistence.repository import Repository


class FakeRepository(Repository):
    def save_fizz_buzz_answer(self, answer: FizzBuzzAnswer):
        pass
