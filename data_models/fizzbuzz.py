from dataclasses import dataclass


@dataclass
class FizzBuzzStandard:
    start: int
    end: int


@dataclass
class FizzBuzzCustom:
    start: int
    end: int
    fizz: int
    buzz: int


FizzBuzzInput = FizzBuzzStandard | FizzBuzzCustom


@dataclass
class FizzBuzzAnswer:
    start: int
    end: int
    fizz: int
    buzz: int
    answer: [str]
