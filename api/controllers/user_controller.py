import logging
from fastapi import Depends

# Models
from api.models.user_models import UserCreate, UserUpdate, User

# Services
from api.services.user_services import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user,
)

# Utils
from api.utils.auth_utils import get_password_hash


logger = logging.getLogger("api")


async def add_user(user: UserCreate = Depends()):
    data = user.dict()
    data["password"] = get_password_hash(data["password"])

    try:
        newUser = await create_user(data)
        return User(**newUser.dict())
    except Exception as e:
        raise e


async def get_all_users():
    try:
        users = await get_users()
        return [User(**user.dict()) for user in users]
    except Exception as e:
        raise e


async def get_user_by_id(user_id: str):
    try:
        user = await get_user(user_id)
        return User(**user.dict())
    except Exception as e:
        raise e


async def update_user_by_id(user_id: str, user: UserUpdate = Depends()):
    data = {k: v for k, v in user.dict().items() if v is not None}

    if data.get("password"):
        data["password"] = get_password_hash(data["password"])

    try:
        updatedUser = await update_user(user_id, data)
        return User(**updatedUser.dict())
    except Exception as e:
        raise e


async def delete_user_by_id(user_id: str):
    try:
        await delete_user(user_id)
    except Exception as e:
        raise e
