# src/models/user.py
from typing import Optional, Annotated

from pydantic import BaseModel, EmailStr, Field, ConfigDict, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]


class User(BaseModel):
    uuid:  PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jane.doe@example.com",
            }
        }


class UpdateUser(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """

    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "first_name": "Jane Doe",
                "last_name": "Jane Doe",
                "email": "jdoe@example.com",
            }
        },
    )
