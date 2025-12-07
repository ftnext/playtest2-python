import threading
import time

import uvicorn
from fastapi import FastAPI
from getgauge.python import before_suite

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World"}


@before_suite
def start_app():
    server_thread = threading.Thread(target=uvicorn.run, args=(app,), kwargs={"port": 8000}, daemon=True)
    server_thread.start()
    time.sleep(1)
