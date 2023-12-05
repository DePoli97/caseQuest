from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from modules.tests_generator import generate_tests, read_file
from modules.save_results import append_result

app = FastAPI()
read_file()


class FormDataModel(BaseModel):
    age: int
    gender: str
    experience: int


@app.get("/")
async def root():
    return FileResponse("landing.html")


@app.get("/tests")
async def tests():
    return generate_tests()


@app.post("/result")
async def result(
        form_data: FormDataModel,
        current_test: str,
        answer: str,
        time: int,
):
    test_result = {"form_data": form_data, "current_test": current_test, "answer": answer, "time": time}
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
