# app/api/user.py
from uuid import UUID

from fastapi import APIRouter, HTTPException, Depends
from app.models.user import User
from app.services.user_service import UserService

router = APIRouter()


@router.post("/user")
async def create_user(user: User, user_service: UserService = Depends(UserService)):
    user_service.create_user(user)
    return {"message": "User created successfully"}


@router.get("/user/{uuid}")
async def get_user(uuid: UUID, user_service: UserService = Depends(UserService)):
    return user_service.get_user(uuid)


@router.put("/user/{uuid}")
async def update_user(uuid: UUID, updated_user: User, user_service: UserService = Depends(UserService)):
    user_service.update_user(uuid, updated_user)
    return {"message": "User updated successfully"}


@router.delete("/user/{uuid}")
async def delete_user(uuid: UUID, user_service: UserService = Depends(UserService)):
    user_service.delete_user(uuid)
    return {"message": "User deleted successfully"}


@router.get("/users")
async def get_all_users(user_service: UserService = Depends(UserService)):
    return user_service.get_all_users()
