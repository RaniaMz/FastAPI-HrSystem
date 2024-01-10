# app/services/user_service.py

from app.models.user import User
from app.repositories.user_repository import UserRepository
from fastapi import HTTPException
from uuid import UUID
from typing import List


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User):
        self.user_repository.create_user(user)

    def get_user(self, uuid: UUID) -> User:
        user = self.user_repository.get_user(uuid)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def update_user(self, uuid: UUID, updated_user: User):
        existing_user = self.user_repository.get_user(uuid)
        if existing_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        self.user_repository.update_user(uuid, updated_user)

    def delete_user(self, uuid: UUID):
        existing_user = self.user_repository.get_user(uuid)
        if existing_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        self.user_repository.delete_user(uuid)

    def get_all_users(self) -> List[User]:
        return self.user_repository.get_all_users()
