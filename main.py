from fastapi import FastAPI
from fastapi.responses import FileResponse
import tests_generator

app = FastAPI()
tests_generator.read_file()

@app.get("/")
async def root():
    return FileResponse("landing.html")


@app.get("/tests")
async def tests():
    return tests_generator.generateTests()

# @app.post("/result")
# async def result(
#
# )


# @app.post("/experiment", (req, res) => {
#     const { spawn } = require('child_process');
#     const pyProg = spawn('python', ['./main.py']);


@app.get("/{file}")
async def files(file: str):
    return FileResponse(f"{file}.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

