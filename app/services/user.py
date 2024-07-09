from app.db.database import db
from app.schemas.user import UserCreate, UserInDB
from app.core.security import get_password_hash, verify_password, create_access_token
from bson.objectid import ObjectId
import motor.motor_asyncio

async def create_user(user: UserCreate):
    user_dict = user.dict()
    user_dict['hashed_password'] = get_password_hash(user_dict.pop('password'))
    result = await db.users.insert_one(user_dict)
    return UserInDB(**user_dict, id=str(result.inserted_id))

async def get_user(username: str):
    user = await db.users.find_one({"username": username})
    if user:
        return UserInDB(**user, id=str(user["_id"]))
    return None

async def authenticate_user(username: str, password: str):
    user = await get_user(username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user