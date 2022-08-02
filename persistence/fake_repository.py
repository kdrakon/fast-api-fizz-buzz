import asyncio

from data_models.fizzbuzz import FizzBuzzAnswer
from persistence.repository import Repository


class FakeRepository(Repository):

    def __init__(self):
        self.__db = dict()

    async def save_fizz_buzz_answer(self, key: str, answer: FizzBuzzAnswer):
        self.__db.update({key: answer})
        await asyncio.sleep(3)  # a slow DB
