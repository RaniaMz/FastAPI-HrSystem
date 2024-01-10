# app/repositories/user_repository.py

from app.models.user import User
from typing import List
from uuid import UUID


class UserRepository:
    users: List[User] = []

    def create_user(self, user: User):
        self.users.append(user)

    def get_user(self, uuid: UUID) -> User:
        for user in self.users:
            if user.uuid == uuid:
                return user
        return None

    def update_user(self, uuid: UUID, updated_user: User):
        for i, user in enumerate(self.users):
            if user.uuid == uuid:
                self.users[i] = updated_user
                return

    def delete_user(self, uuid: UUID):
        self.users = [user for user in self.users if user.uuid != uuid]

    def get_all_users(self) -> List[User]:
        return self.users
