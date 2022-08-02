# fast-api-fizz-buzz

Demonstrates a simple set up of [FastAPI](https://fastapi.tiangolo.com/) to produce [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz#Programming).

To start the app:
```shell
python -m uvicorn main:app --reload
```
API docs available at `http://localhost:8000/docs`

## Example

```http request
POST http://localhost:8000/fizzbuzz
Accept: application/json
Content-Type: application/json

{
  "start": 23,
  "end": 52,
  "fizz": 7,
  "buzz": 8
}

```

Response:
```json
{
  "answer": [
    "23",
    "buzz",
    "25",
    "26",
    "27",
    "fizz",
    "29",
    "30",
    "31",
    "buzz",
    "33",
    "34",
    "fizz",
    "36",
    "37",
    "38",
    "39",
    "buzz",
    "41",
    "fizz",
    "43",
    "44",
    "45",
    "46",
    "47",
    "buzz",
    "fizz",
    "50",
    "51",
    "52"
  ]
}
```
