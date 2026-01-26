from fastapi import FastAPI
from routes import tasks # <--- Import the new file

app = FastAPI()

# Plug in the "Tasks" power strip
app.include_router(tasks.router)

@app.get("/")
def home():
    return {"message": "Backend is running with Routers!"}
