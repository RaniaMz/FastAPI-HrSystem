# src/tests/test_user_service.py

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from uuid import uuid4


def test_create_user():
    service = UserService(UserRepository())
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4()
    )

    service.create_user(user)
    assert len(service.user_repository.users) == 1


def test_get_user():
    service = UserService(UserRepository())
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4()
    )

    service.create_user(user)
    retrieved_user = service.get_user(user.uuid)
    assert retrieved_user == user


def test_update_user():
    service = UserService(UserRepository())
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4()
    )

    service.create_user(user)
    updated_user = User(
        first_name="Updated John",
        last_name="Updated Doe",
        email="updated.john.doe@example.com",
        uuid=user.uuid
    )

    service.update_user(user.uuid, updated_user)
    assert service.get_user(user.uuid) == updated_user


def test_delete_user():
    service = UserService(UserRepository())
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4()
    )

    service.create_user(user)
    service.delete_user(user.uuid)
    assert len(service.user_repository.users) == 0


def test_get_all_users():
    service = UserService(UserRepository())
    user1 = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4()
    )

    user2 = User(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        uuid=uuid4()
    )

    service.create_user(user1)
    service.create_user(user2)

    all_users = service.get_all_users()
    assert len(all_users) == 2
