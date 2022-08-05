from fastapi import FastAPI

from data_models.api_models import FizzBuzzRequest, to_fizz_buzz_input, FizzBuzzResponse, to_fizz_buzz_output
from data_models.fizzbuzz import FizzBuzzAnswer
from persistence.fake_repository import FakeRepository
from persistence.repository import Repository
from service.fizzbuzz_service import FizzBuzzService

app: FastAPI = FastAPI()

# dependency graph
repository: Repository = FakeRepository()
fizzbuzz_service: FizzBuzzService = FizzBuzzService(repository)


# APIs
@app.get("/status")
async def status():
    return {"status": "ok"}


@app.post("/fizzbuzz", response_model=FizzBuzzResponse)
async def post_fizz_buzz(body: FizzBuzzRequest) -> FizzBuzzResponse:
    answer: FizzBuzzAnswer = await fizzbuzz_service.compute(to_fizz_buzz_input(body))
    return to_fizz_buzz_output(answer)
