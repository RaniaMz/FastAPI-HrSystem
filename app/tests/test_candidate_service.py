# src/tests/test_candidate_service.py

from app.models.candidate import Candidate
from app.repositories.candidate_repository import CandidateRepository
from app.services.candidate_service import CandidateService
from uuid import uuid4


def test_create_candidate():
    service = CandidateService(CandidateRepository())
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

    service.create_candidate(candidate)
    assert len(service.candidate_repository.candidates) == 1


def test_get_candidate():
    service = CandidateService(CandidateRepository())
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

    service.create_candidate(candidate)
    retrieved_candidate = service.get_candidate(candidate.uuid)
    assert retrieved_candidate == candidate


def test_update_candidate():
    service = CandidateService(CandidateRepository())
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

    service.create_candidate(candidate)
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

    service.update_candidate(candidate.uuid, updated_candidate)
    assert service.get_candidate(candidate.uuid) == updated_candidate


def test_delete_candidate():
    service = CandidateService(CandidateRepository())
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

    service.create_candidate(candidate)
    service.delete_candidate(candidate.uuid)
    assert len(service.candidate_repository.candidates) == 0


def test_get_all_candidates():
    service = CandidateService(CandidateRepository())
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

    service.create_candidate(candidate1)
    service.create_candidate(candidate2)

    all_candidates = service.get_all_candidates()
    assert len(all_candidates) == 2
