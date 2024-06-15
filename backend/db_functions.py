import bcrypt
import os
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

# MongoDB connection
MONGO_DETAILS = os.getenv("MONGO_URI")
if MONGO_DETAILS is None:
    raise ValueError("MONGO_URI is not set in the environment variables")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client['cfg_test']
user_collection = database['cfg_users']


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