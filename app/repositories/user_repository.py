# src/repositories/user_repository.py
import pydantic
from bson import ObjectId
from fastapi import HTTPException
from starlette import status

from app.db.mongodb import db
from app.models.user import User, UpdateUser
from typing import List


class UserRepository:

    async def create_user(self, user: User) -> User:
        user_collection = db.client.get_database().get_collection('users')

        new_user = await user_collection.insert_one(user.model_dump())

        created_user = await user_collection.find_one(
            {"_id": new_user.inserted_id}
        )
        return created_user

    async def get_user(self, id: str) -> User:
        user_collection = db.client.get_database().get_collection('users')

        try:
            user_id = ObjectId(id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid user ID format: {e}"
            )

        user = await user_collection.find_one({
            "_id": user_id
        })

        if user:
            return user

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {id} not found"
        )

    async def update_user(self, id: str, user: UpdateUser) -> UpdateUser:
        user_collection = db.client.get_database().get_collection('users')

        try:
            user_id = ObjectId(id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid user ID format: {e}"
            )

        result = await user_collection.update_one(
            {"_id": user_id},
            {"$set": user.model_dump(exclude_unset=True)}
        )

        updated_user = await user_collection.find_one({"_id": user_id})

        if updated_user:
            return updated_user

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {id} not found"
        )

    async def delete_user(self, id: str) -> str:
        user_collection = db.client.get_database().get_collection('users')

        try:
            user_id = ObjectId(id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid user ID format: {e}"
            )

        user = await user_collection.find_one({
            "_id": user_id
        })

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        await user_collection.delete_one({"_id": user_id})
        return f"User with ID {id} has been deleted"

    async def get_all_users(self) -> List[User]:
        users: List[User] = []
        user_collection = db.client.get_database().get_collection('users')

        user_documents = user_collection.find({})
        async for row in user_documents:
            users.append(User(**row, ))
        return users
