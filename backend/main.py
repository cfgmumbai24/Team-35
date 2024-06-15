from fastapi import FastAPI, HTTPException, Request, Form, Depends, Query
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# MongoDB connection
MONGO_DETAILS = os.getenv("MONGO_URI")
if MONGO_DETAILS is None:
    raise ValueError("MONGO_URI is not set in the environment variables")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client['cfg_test']
user_collection = database['cfg_users']

# Pydantic models
class UserInDB(BaseModel):
    name: str
    phone_number: str
    age: Optional[int]
    gender: Optional[str]
    income: Optional[float]
    hashed_password: str

class User(BaseModel):
    name: str = Field(..., example="John Doe")
    phone_number: str = Field(..., example="+1234567890")
    age: Optional[int] = Field(None, example=30)
    gender: Optional[str] = Field(None, example="Male")
    income: Optional[float] = Field(None, example=50000.0)

class UserCreate(User):
    password: str = Field(..., example="strongpassword123")

class UserLogin(BaseModel):
    phone_number: str = Field(..., example="+1234567890")
    password: str = Field(..., example="strongpassword123")

class UserResponse(BaseModel):
    id: str
    name: str
    phone_number: str
    age: Optional[int]
    gender: Optional[str]
    income: Optional[float]

# Helper functions
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "phone_number": user["phone_number"],
        "age": user.get("age"),
        "gender": user.get("gender"),
        "income": user.get("income")
    }

async def get_user(phone_number: str):
    user = await user_collection.find_one({"phone_number": phone_number})
    if user:
        return user_helper(user)

async def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

async def insert_user(user: dict) -> dict:
    new_user = await user_collection.insert_one(user)
    created_user = await user_collection.find_one({"_id": new_user.inserted_id})
    return user_helper(created_user)

@app.post("/signup", response_model=UserResponse)
async def create_user(user: UserCreate):
    if await user_collection.find_one({"phone_number": user.phone_number}):
        raise HTTPException(status_code=400, detail="Phone number already registered")

    hashed_password = await hash_password(user.password)
    user_dict = user.dict()
    user_dict['hashed_password'] = hashed_password
    del user_dict['password']

    created_user = await insert_user(user_dict)
    return created_user

@app.post("/login")
async def login(phone_number: str = Query(...), password: str = Query(...)):
    db_user = await user_collection.find_one({"phone_number": phone_number})
    if db_user and await verify_password(password, db_user['hashed_password']):
        return user_helper(db_user)
    raise HTTPException(status_code=400, detail="Invalid phone number or password")

@app.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: str):
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_helper(user)
    raise HTTPException(status_code=404, detail="User not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



# http request, post and get could be together