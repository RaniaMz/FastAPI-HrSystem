# src/services/user_service.py

from app.models.user import User, UpdateUser
from app.repositories.user_repository import UserRepository
from fastapi import HTTPException, Depends


def is_user_authorized_all_candidates(user: User) -> bool:
    return 'admin' in user.roles


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def create_user(self, user: User):
        return await self.user_repository.create_user(user)

    async def get_user(self, id: str):
        user = await self.user_repository.get_user(id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def update_user(self, id: str, updated_user: UpdateUser):
        existing_user = await self.user_repository.get_user(id)
        if existing_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return await self.user_repository.update_user(id, updated_user)

    async def delete_user(self, id: str):
        existing_user = await self.user_repository.get_user(id)
        if existing_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return await self.user_repository.delete_user(id)

    async def get_all_users(self):
        return await self.user_repository.get_all_users()
