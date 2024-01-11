# src/tests/test_user_repository.py

from app.models.user import User
from app.repositories.user_repository import UserRepository
from uuid import uuid4


def test_create_user():
    repository = UserRepository()
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4()
    )

    repository.create_user(user)
    assert len(repository.users) == 1


def test_get_user():
    repository = UserRepository()
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4()
    )

    repository.create_user(user)
    retrieved_user = repository.get_user(user.uuid)
    assert retrieved_user == user


def test_update_user():
    repository = UserRepository()
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4()
    )

    repository.create_user(user)
    updated_user = User(
        first_name="Updated John",
        last_name="Updated Doe",
        email="updated.john.doe@example.com",
        uuid=user.uuid
    )

    repository.update_user(user.uuid, updated_user)
    assert repository.get_user(user.uuid) == updated_user


def test_delete_user():
    repository = UserRepository()
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4()
    )

    repository.create_user(user)
    repository.delete_user(user.uuid)
    assert len(repository.users) == 0


def test_get_all_users():
    repository = UserRepository()
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

    repository.create_user(user1)
    repository.create_user(user2)

    all_users = repository.get_all_users()
    assert len(all_users) == 2
