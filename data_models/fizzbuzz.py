from dataclasses import dataclass


@dataclass
class FizzBuzzStandard:
    start: int
    end: int


@dataclass
class FizzBuzzCustom(FizzBuzzStandard):
    start: int
    end: int
    fizz: int
    buzz: int


@dataclass
class FizzBuzzAnswer:
    start: int
    end: int
    fizz: int
    buzz: int
    answer: [str]
