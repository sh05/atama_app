from typing import List
from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from detect import detect_obj

app = FastAPI()

app.mount("/think", StaticFiles(directory="/app/html/", html=True), name="html")
app.mount("/static", StaticFiles(directory="/app/static/"), name="static")
# app.mount("/img", StaticFiles(directory=FRONT_DIR + "/img", html=True), name="img")
# app.mount("/", StaticFiles(directory=FRONT_DIR, html=True), name="html")

@app.post("/lookat")
async def read_root(obj: UploadFile = File(...)):
    obj_name = detect_obj(await obj.read())
    print(obj_name)
    return {
            "kashiko": [],
            "warui": [],
            }
