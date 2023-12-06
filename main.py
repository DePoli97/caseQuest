from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from modules.tests_generator import generate_tests, read_file, generate_camel_tests, generate_kebab_tests
from modules.save_results import append_result
from modules.user_identifier import get_last_id, increment_last_id

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
read_file()


class ResultModel(BaseModel):
    id: int
    age: int
    gender: str
    experience: int
    case_type: str
    is_correct_answer: bool
    time: int


@app.get("/")
async def root():
    return FileResponse("landing.html")


@app.get("/tests")
async def tests():
    all_tests = generate_tests()
    camel_tests = generate_camel_tests(all_tests)
    kebab_tests = generate_kebab_tests(all_tests)
    return camel_tests, kebab_tests


@app.post("/result")
async def result(test_result: ResultModel):
    print(test_result)
    return append_result(test_result)


@app.get("/last_test_id")
async def last_test_id():
    return get_last_id()


@app.get("/update_last_test_id")
async def last_test_id():
    increment_last_id()
    return "Last test id updated"

# @app.post("/experiment", (req, res) => {
#     const { spawn } = require('child_process');
#     const pyProg = spawn('python', ['./main.py']);


@app.get("/{file}")
async def files(file: str):
    return FileResponse(f"{file}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
