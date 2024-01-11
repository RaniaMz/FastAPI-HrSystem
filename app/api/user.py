# src/api/user.py
from fastapi import APIRouter, HTTPException
from starlette import status
from app.models.user import User, UpdateUser
from app.services.user_service import UserService

router = APIRouter()


@router.post("/user",
             response_description='create user',
             status_code=status.HTTP_201_CREATED,
             response_model=User,
             tags=['User Section'])
async def create_user(user: User):
    try:
        return await UserService().create_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/user/{id}",
            response_description='get user',
            status_code=status.HTTP_200_OK,
            response_model=User,
            tags=['User Section'])
async def get_user(id: str):
    try:

        return await UserService().get_user(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.put("/user/{id}",
            response_description='update user',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=UpdateUser,
            tags=['User Section'])
async def update_user(id: str, updated_user: UpdateUser):
    try:
        return await UserService().update_user(id, updated_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.delete("/user/{id}",
               response_description='Delete user',
               status_code=status.HTTP_200_OK,
               response_model=str,
               tags=['User Section'])
async def delete_user(id: str):
    try:
        return await UserService().delete_user(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/users",
            response_description="List all users",
            status_code=status.HTTP_200_OK,
            tags=['User Section'])
async def get_all_users():
    return await UserService().get_all_users()
