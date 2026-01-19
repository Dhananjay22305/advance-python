from fastapi import FastAPI

app = FastAPI(title="Student Productivity Dashboard")
print("main.py loaded")

@app.get("/")
def root():
    return {"status": "API running"}
