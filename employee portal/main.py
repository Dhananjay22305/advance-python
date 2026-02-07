from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm      # For handling OAuth2 authentication
from jose import JWTError, jwt    # For encoding and decoding JWT tokens
from passlib.context import CryptContext    # For hashing and verifying passwords
from datetime import datetime, timedelta

# --- CONFIGURATION ---
SECRET_KEY = "my_super_secret_key" # In real life, keep this in an .env file
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app = FastAPI()

# --- MOCK DATABASE ---
users_db = {
    "alice@startup.com": {
        "email": "alice@startup.com",
        "hashed_password": pwd_context.hash("secret123"),
        "role": "admin"
    },
    "bob@startup.com": {
        "email": "bob@startup.com",
        "hashed_password": pwd_context.hash("password456"),
        "role": "employee"
    }
}

# --- UTILS: Security Logic ---
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        role: str = payload.get("role")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"email": email, "role": role}
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

# --- ENDPOINTS ---

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not pwd_context.verify(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    # We put the email (sub) and role in the token
    token = create_access_token(data={"sub": user["email"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/profile")
async def get_profile(current_user: dict = Depends(get_current_user)):
    return {"message": "Welcome to your profile", "user": current_user}

@app.get("/employees")
async def get_employees(current_user: dict = Depends(get_current_user)):
    # Role-Based Access Control (RBAC)
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admins can see the employee list")
    
    return {"employees": ["Alice (Admin)", "Bob (Developer)", "Charlie (Designer)"]}