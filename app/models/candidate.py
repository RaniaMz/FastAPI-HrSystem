# app/models/candidate.py

from pydantic import BaseModel
from typing import List
from uuid import UUID


class Candidate(BaseModel):
    first_name: str
    last_name: str
    email: str
    uuid: UUID
    career_level: str
    job_major: str
    years_of_experience: int
    degree_type: str
    skills: List[str]
    nationality: str
    city: str
    salary: float
    gender: List[str]
