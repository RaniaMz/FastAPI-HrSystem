# app/tests/test_candidate_repository.py

from app.models.candidate import Candidate
from app.repositories.candidate_repository import CandidateRepository
from uuid import uuid4

def test_create_candidate():
    repository = CandidateRepository()
    candidate = Candidate(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4(),
        career_level="Senior",
        job_major="Computer Science",
        years_of_experience=5,
        degree_type="Master",
        skills=["Python", "FastAPI"],
        nationality="US",
        city="New York",
        salary=100000.0,
        gender=["Male"]
    )

    repository.create_candidate(candidate)
    assert len(repository.candidates) == 1

def test_get_candidate():
    repository = CandidateRepository()
    candidate = Candidate(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4(),
        career_level="Senior",
        job_major="Computer Science",
        years_of_experience=5,
        degree_type="Master",
        skills=["Python", "FastAPI"],
        nationality="US",
        city="New York",
        salary=100000.0,
        gender=["Male"]
    )

    repository.create_candidate(candidate)
    retrieved_candidate = repository.get_candidate(candidate.uuid)
    assert retrieved_candidate == candidate

def test_update_candidate():
    repository = CandidateRepository()
    candidate = Candidate(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4(),
        career_level="Senior",
        job_major="Computer Science",
        years_of_experience=5,
        degree_type="Master",
        skills=["Python", "FastAPI"],
        nationality="US",
        city="New York",
        salary=100000.0,
        gender=["Male"]
    )

    repository.create_candidate(candidate)
    updated_candidate = Candidate(
        first_name="Updated John",
        last_name="Updated Doe",
        email="updated.john.doe@example.com",
        uuid=candidate.uuid,
        career_level="Senior",
        job_major="Computer Science",
        years_of_experience=6,
        degree_type="Master",
        skills=["Python", "FastAPI", "Docker"],
        nationality="US",
        city="New York",
        salary=110000.0,
        gender=["Male"]
    )

    repository.update_candidate(candidate.uuid, updated_candidate)
    assert repository.get_candidate(candidate.uuid) == updated_candidate


def test_delete_candidate():
    repository = CandidateRepository()
    candidate = Candidate(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4(),
        career_level="Senior",
        job_major="Computer Science",
        years_of_experience=5,
        degree_type="Master",
        skills=["Python", "FastAPI"],
        nationality="US",
        city="New York",
        salary=100000.0,
        gender=["Male"]
    )

    repository.create_candidate(candidate)
    repository.delete_candidate(candidate.uuid)
    assert len(repository.candidates) == 0


def test_get_all_candidates():
    repository = CandidateRepository()
    candidate1 = Candidate(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        uuid=uuid4(),
        career_level="Senior",
        job_major="Computer Science",
        years_of_experience=5,
        degree_type="Master",
        skills=["Python", "FastAPI"],
        nationality="US",
        city="New York",
        salary=100000.0,
        gender=["Male"]
    )

    candidate2 = Candidate(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        uuid=uuid4(),
        career_level="Junior",
        job_major="Data Science",
        years_of_experience=2,
        degree_type="Bachelor",
        skills=["Python", "SQL"],
        nationality="UK",
        city="London",
        salary=80000.0,
        gender=["Female"]
    )

    repository.create_candidate(candidate1)
    repository.create_candidate(candidate2)

    all_candidates = repository.get_all_candidates()
    assert len(all_candidates) == 2
