# main.py
import logging
import time 

# 2. Force the logger to use Local Time (Computer time) instead of GMT
logging.Formatter.converter = time.localtime 

from fastapi import FastAPI
from routes import tasks


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S" # Optional: Makes the date look cleaner
)

app = FastAPI()

app = FastAPI()

# Plug in the "Tasks" power strip
app.include_router(tasks.router)

@app.get("/")
def home():
    return {"message": "Backend is running with Routers!"}
