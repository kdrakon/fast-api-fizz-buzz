from dataclasses import dataclass, field
from typing import List

from data_models.fizzbuzz import FizzBuzzStandard, FizzBuzzCustom, FizzBuzzAnswer, FizzBuzzInput


@dataclass
class FizzBuzzRequest:
    start: int
    end: int
    fizz: int | None = None
    buzz: int | None = None


@dataclass
class FizzBuzzResponse:
    answer: List[str] = field(default_factory=list)


def to_fizz_buzz_input(request: FizzBuzzRequest) -> FizzBuzzInput:
    match (request.fizz, request.buzz):
        case (None, None) | (None, _) | (_, None):
            return FizzBuzzStandard(request.start, request.end)
        case (fizz, buzz) if type(fizz) is int and type(buzz) is int:  # I would rather create a class like `Some`, but then I lose the JSON serialisation
            return FizzBuzzCustom(request.start, request.end, fizz, buzz)


def to_fizz_buzz_output(answer: FizzBuzzAnswer) -> FizzBuzzResponse:
    return FizzBuzzResponse(answer.answer)
