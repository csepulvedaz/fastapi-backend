import logging

# Config
from api.core.prisma import prisma

logger = logging.getLogger("api")


async def create_user(user: dict):
    logger.info("Creating users")
    return await prisma.user.create(data=user)


async def get_users():
    logger.info("Getting all users")
    return await prisma.user.find_many()


async def get_user(user_id: str):
    logger.info(f"Getting user with id {user_id}")
    return await prisma.user.find_unique(where={"id": user_id})


async def get_user_by_email(user_email: str):
    logger.info(f"Getting user with email {user_email}")
    return await prisma.user.find_unique(where={"email": user_email})


async def update_user(user_id: str, user: dict):
    logger.info(f"Updating user with id {user_id}")
    return await prisma.user.update(where={"id": user_id}, data=user)


async def delete_user(user_id: str):
    logger.info(f"Deleting user with id {user_id}")
    return await prisma.user.delete(where={"id": user_id})
