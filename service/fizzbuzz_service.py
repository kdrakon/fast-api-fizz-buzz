from data_models.fizzbuzz import FizzBuzzStandard, FizzBuzzAnswer
from persistence.repository import Repository
from service import functions


class FizzBuzzService:

    def __init__(self, repository: Repository):
        self.repository = repository

    def compute(self, fizzbuzz: FizzBuzzStandard) -> FizzBuzzAnswer:
        answer = functions.compute(fizzbuzz)
        self.repository.save_fizz_buzz_answer(answer)
        return answer
