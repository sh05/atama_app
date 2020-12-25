from typing import List
from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/think", StaticFiles(directory="/app/html/", html=True), name="html")
app.mount("/static", StaticFiles(directory="/app/static/"), name="static")
# app.mount("/img", StaticFiles(directory=FRONT_DIR + "/img", html=True), name="img")
# app.mount("/", StaticFiles(directory=FRONT_DIR, html=True), name="html")

@app.post("/lookat")
async def read_root(obj: UploadFile = File(...)):
    # image = load_image_into_numpy_array(await file.read())
    print(obj)
    # print(image)
    return {
            "kashiko": ["hello", "konnnitiha"],
            "warui": [""],
            }
