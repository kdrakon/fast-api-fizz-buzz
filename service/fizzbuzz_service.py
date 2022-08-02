from data_models.fizzbuzz import FizzBuzzStandard, FizzBuzzAnswer
from persistence.repository import Repository
from service import functions


class FizzBuzzService:

    def __init__(self, repository: Repository):
        self.repository = repository

    async def compute(self, fizzbuzz: FizzBuzzStandard) -> FizzBuzzAnswer:
        answer = functions.compute(fizzbuzz)
        key = functions.key_for_answer(answer)
        await self.repository.save_fizz_buzz_answer(key, answer)
        return answer
