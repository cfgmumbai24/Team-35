from fastapi import FastAPI,File,UploadFile,Form, Request, Query, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import os
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
import bcrypt
from bson import ObjectId

from language import translation, transcribe, text_to_speech
from chatbot import ask_llm
from update_lang import update_json_values

import json

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "*"
#     ]
# )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    # access-control-allow-origin=["*"]
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://127.0.0.1:5000"],  # Replace with your frontend URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



# message: str = Form(...), language: str = Form(...)
# request: Request
@app.post('/chat_text')
async def chat_text(request: Request):
    try: 
        data = await request.json()
        language = data['language']
        message = data['message']
        if(language != "English"):
            message_english = await translation(language, "English", message)
            message_english_text = message_english['translated_content']
        else:
            message_english_text = message
        print(f"Message:\n{message_english_text}")
        answer = await ask_llm(message_english_text)
        print(f"\n\nAnswer: {answer}")
        if(language != "English"):
            answer_translate = await translation("English", language, answer)
            answer_translate_text = answer_translate['translated_content']
        else:
            answer_translate_text = answer

        print(f"\n\nafter:{answer_translate_text}")
        return JSONResponse(content={"message": answer_translate_text, "success": True}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": "Error in running chat_text", "success": False}, status_code=500)
    
# language: str = Form(...)
@app.post('/prefetch_login')
async def prefetch_login(request: Request):
    try:

        language = request.json()
        f = open('static_data.json')
        print(f)
        data = json.load(f)
        lang_data = await update_json_values(data, language)
        print(data)
        return JSONResponse(content={"message": lang_data, "success": True}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": "Failed during trying prefetch_login", "success": False}, status_code=500)

# /fetch_pre_login
# /post_login


templates = Jinja2Templates(directory="templates")

# MongoDB connection
MONGO_DETAILS = os.getenv("MONGO_URI")
if MONGO_DETAILS is None:
    raise ValueError("MONGO_URI is not set in the environment variables")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client['cfg_test']
user_collection = database['cfg_users']

class UserInDB(BaseModel):
    name: str
    password: str
    # name: str
    # password: str  # Add this field
    phone_number: str
    # age: Optional[int]
    # gender: Optional[str]
    # income: Optional[float]
    # hashed_password: Optional[str] = None  # Optional hashed_password field


# class User(BaseModel):
#     name: str = Field(..., example="John Doe")
#     phone_number: str = Field(..., example="+1234567890")
#     age: Optional[int] = Field(None, example=30)
#     gender: Optional[str] = Field(None, example="Male")
#     income: Optional[float] = Field(None, example=50000.0)

# class UserCreate(User):
#     password: str = Field(..., example="strongpassword123")

class UserLogin(BaseModel):
    phone_number: str = Field(..., example="+1234567890")
    password: str = Field(..., example="strongpassword123")

class UserResponse(BaseModel):
    # id: str
    name: str
    password: str
    phone_number: str
    age: Optional[int]
    gender: Optional[str]
    income: Optional[float]

# Helper functions
def user_helper(user) -> dict:
    return {
        # "id": str(user["_id"]),
        "name": user["name"],
        "password": user["hashed_password"],
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
    print(">> ", created_user)
    return user_helper(created_user)

# @app.post("/signup", response_model=UserResponse)
# async def create_user(user: UserInDB):
#     if await user_collection.find_one({"phone_number": user.phone_number}):
#         raise HTTPException(status_code=400, detail="Phone number already registered")

#     hashed_password = await hash_password(user.password)
#     user_dict = user.dict()
#     user_dict['hashed_password'] = hashed_password
#     del user_dict['password']

#     created_user = await insert_user(user_dict)
#     return created_user


@app.post("/signup", response_model=UserResponse)
async def create_user(user: UserInDB):
    print(">>>> ", user)
    if await user_collection.find_one({"phone_number": user.phone_number}):
        raise HTTPException(status_code=400, detail="Phone number already registered")

    hashed_password = await hash_password(user.password)
    print(">> user===> ", user.dict(), type(user.dict()))
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

# @app.post("/reward_update")
# async def update_reward()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)



# http request, post and get could be together