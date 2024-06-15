# from fastapi import FastAPI, HTTPException, Depends, Form
# from pydantic import BaseModel, EmailStr, Field
# from typing import Optional
# from motor.motor_asyncio import AsyncIOMotorClient
# from bson import ObjectId
# import bcrypt
# import os

# app = FastAPI()

# # MongoDB connection
# MONGO_DETAILS = "mongodb+srv://chatvibe0707:chatvibe0707@cluster0.bkhneqo.mongodb.net/?retryWrites=true&w=majority"
# client = AsyncIOMotorClient(MONGO_DETAILS)
# database = client['cfg_test']
# user_collection = database['cfg_users']

# # Pydantic models
# class UserInDB(BaseModel):
#     name: str
#     phone_number: str
#     age: Optional[int]
#     gender: Optional[str]
#     income: Optional[float]
#     hashed_password: str

# class User(BaseModel):
#     name: str
#     phone_number: str
#     age: Optional[int]
#     gender: Optional[str]
#     income: Optional[float]
#     password: str

# class UserLogin(BaseModel):
#     phone_number: str
#     password: str

# class UserResponse(BaseModel):
#     id: str
#     name: str
#     phone_number: str
#     age: Optional[int]
#     gender: Optional[str]
#     income: Optional[float]

# # Helper functions
# def user_helper(user) -> dict:
#     return {
#         "id": str(user["_id"]),
#         "name": user["name"],
#         "phone_number": user["phone_number"],
#         "age": user.get("age"),
#         "gender": user.get("gender"),
#         "income": user.get("income")
#     }

# async def get_user(phone_number: str):
#     user = await user_collection.find_one({"phone_number": phone_number})
#     if user:
#         return user_helper(user)

# async def hash_password(password: str) -> str:
#     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# async def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# @app.post("/signup", response_model=UserResponse)
# async def create_user(user: User):
#     if await user_collection.find_one({"phone_number": user.phone_number}):
#         raise HTTPException(status_code=400, detail="Phone number already registered")

#     hashed_password = await hash_password(user.password)
#     user_dict = user.dict()
#     user_dict['hashed_password'] = hashed_password
#     del user_dict['password']

#     new_user = await user_collection.insert_one(user_dict)
#     created_user = await user_collection.find_one({"_id": new_user.inserted_id})
#     return user_helper(created_user)

# @app.post("/login")
# async def login(user: UserLogin):
#     db_user = await user_collection.find_one({"phone_number": user.phone_number})
#     if db_user and await verify_password(user.password, db_user['hashed_password']):
#         return user_helper(db_user)
#     raise HTTPException(status_code=400, detail="Invalid phone number or password")

# @app.get("/users/{user_id}", response_model=UserResponse)
# async def read_user(user_id: str):
#     user = await user_collection.find_one({"_id": ObjectId(user_id)})
#     if user:
#         return user_helper(user)
#     raise HTTPException(status_code=404, detail="User not found")
