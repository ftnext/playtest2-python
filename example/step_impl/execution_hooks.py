import threading
import time

import uvicorn
from fastapi import FastAPI
from getgauge.python import before_suite

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World"}


config = uvicorn.Config(app, port=8000)
server = uvicorn.Server(config)


@before_suite
def start_app():
    server_thread = threading.Thread(target=server.run, daemon=True)
    server_thread.start()
    time.sleep(1)
