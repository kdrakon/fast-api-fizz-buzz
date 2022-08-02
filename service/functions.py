from functools import partial

from data_models.fizzbuzz import FizzBuzzStandard, FizzBuzzCustom, FizzBuzzAnswer


def compute(fizzbuzz: FizzBuzzStandard) -> FizzBuzzAnswer:
    match fizzbuzz:
        case FizzBuzzCustom(start, end, fizz, buzz):
            return FizzBuzzAnswer(__fizzbuzz(start, end, fizz, buzz))
        case FizzBuzzStandard(start, end):
            return FizzBuzzAnswer(__fizzbuzz(start, end, 3, 5))


def __fizzbuzz(start: int, end: int, fizz: int, buzz: int) -> [str]:
    listrange: [int] = list(range(start, end + 1))
    return list(map(partial(__fizz_or_buzz_or_retain, fizz, buzz), listrange))


def __fizz_or_buzz_or_retain(fizz: int, buzz: int, i: int) -> str:
    match i:
        case _ if i % fizz == 0:
            return "fizz"
        case _ if i % buzz == 0:
            return "buzz"
        case _:
            return i
