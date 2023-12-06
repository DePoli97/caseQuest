from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from modules.tests_generator import generate_tests, read_file, generate_camel_tests, generate_kebab_tests
from modules.save_results import append_result

app = FastAPI()
read_file()


class ResultModel(BaseModel):
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


# @app.post("/experiment", (req, res) => {
#     const { spawn } = require('child_process');
#     const pyProg = spawn('python', ['./main.py']);


@app.get("/{file}")
async def files(file: str):
    return FileResponse(f"{file}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
