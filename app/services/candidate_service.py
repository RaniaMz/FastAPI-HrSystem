# app/services/candidate_service.py

from app.models.candidate import Candidate
from app.repositories.candidate_repository import CandidateRepository
from fastapi import HTTPException
from uuid import UUID
from typing import List


class CandidateService:
    def __init__(self, candidate_repository: CandidateRepository):
        self.candidate_repository = candidate_repository

    def create_candidate(self, candidate: Candidate):
        self.candidate_repository.create_candidate(candidate)

    def get_candidate(self, uuid: UUID) -> Candidate:
        candidate = self.candidate_repository.get_candidate(uuid)
        if candidate is None:
            raise HTTPException(status_code=404, detail="Candidate not found")
        return candidate

    def update_candidate(self, uuid: UUID, updated_candidate: Candidate):
        existing_candidate = self.candidate_repository.get_candidate(uuid)
        if existing_candidate is None:
            raise HTTPException(status_code=404, detail="Candidate not found")
        self.candidate_repository.update_candidate(uuid, updated_candidate)

    def delete_candidate(self, uuid: UUID):
        existing_candidate = self.candidate_repository.get_candidate(uuid)
        if existing_candidate is None:
            raise HTTPException(status_code=404, detail="Candidate not found")
        self.candidate_repository.delete_candidate(uuid)

    def get_all_candidates(self) -> List[Candidate]:
        return self.candidate_repository.get_all_candidates()
