# src/models/candidate.py
from typing import List, Annotated, Optional

from pydantic import BaseModel, EmailStr, Field, BeforeValidator, ConfigDict

PyObjectId = Annotated[str, BeforeValidator(str)]


class Candidate(BaseModel):
    uuid: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str
    last_name: str
    email: EmailStr
    career_level: str
    job_major: str
    years_of_experience: int
    degree_type: str
    skills: List[str]
    nationality: str
    city: str
    salary: float
    gender: List[str]

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "career_level": "Mid",
                "job_major": "Software Developer",
                "years_of_experience": 5,
                "degree_type": "Bachelor's",
                "skills": ["Python", "JavaScript"],
                "nationality": "US",
                "city": "New York",
                "salary": 80000.0,
                "gender": ["Male"],
            }
        }


class UpdateCandidate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    career_level: Optional[str]
    job_major: Optional[str]
    years_of_experience: Optional[int]
    degree_type: Optional[str]
    skills: Optional[List[str]]
    nationality: Optional[str]
    city: Optional[str]
    salary: Optional[float]
    gender: Optional[List[str]]

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "career_level": "Senior",
                "job_major": "DevOps Engineer",
                "years_of_experience": 7,
                "degree_type": "Master's",
                "skills": ["Docker", "Django"],
                "nationality": "CA",
                "city": "Toronto",
                "salary": 100000.0,
                "gender": ["Male"],
            }
        },
    )