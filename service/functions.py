from functools import partial

from data_models.fizzbuzz import FizzBuzzStandard, FizzBuzzCustom, FizzBuzzAnswer, FizzBuzzInput


def compute(fizzbuzz: FizzBuzzInput) -> FizzBuzzAnswer:
    match fizzbuzz:
        case FizzBuzzCustom(start, end, fizz, buzz):
            return FizzBuzzAnswer(start, end, fizz, buzz, __fizzbuzz(start, end, fizz, buzz))
        case FizzBuzzStandard(start, end):
            return FizzBuzzAnswer(start, end, 3, 5, __fizzbuzz(start, end, 3, 5))


def __fizzbuzz(start: int, end: int, fizz: int, buzz: int) -> list[str]:
    list_range: list[int] = list(range(start, end + 1))
    return list(map(partial(__fizz_or_buzz_or_retain, fizz, buzz), list_range))


def __fizz_or_buzz_or_retain(fizz: int, buzz: int, i: int) -> str:
    match i:
        case _ if i % fizz == 0:
            return "fizz"
        case _ if i % buzz == 0:
            return "buzz"
        case _:
            return f"{i}"


def key_for_answer(answer: FizzBuzzAnswer) -> str:
    return f'{answer.start}-{answer.end}-{answer.fizz}-{answer.buzz}'
