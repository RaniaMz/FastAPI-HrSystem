# src/services/candidate_service.py
from app.models.candidate import Candidate, UpdateCandidate
from app.repositories.candidate_repository import CandidateRepository
from fastapi import HTTPException
from typing import List


class CandidateService:
    def __init__(self):
        self.candidate_repository = CandidateRepository()

    def create_candidate(self, candidate: Candidate):
        return self.candidate_repository.create_candidate(candidate)

    async def get_candidate(self, id: str) -> Candidate:
        candidate = await self.candidate_repository.get_candidate(id)
        if candidate is None:
            raise HTTPException(status_code=404, detail="Candidate not found")
        return candidate

    async def update_candidate(self, id: str, updated_candidate: UpdateCandidate):
        existing_candidate = await self.candidate_repository.get_candidate(id)
        if existing_candidate is None:
            raise HTTPException(status_code=404, detail="Candidate not found")
        return await self.candidate_repository.update_candidate(id, updated_candidate)

    async def delete_candidate(self, id: str):
        existing_candidate = await self.candidate_repository.get_candidate(id)
        if existing_candidate is None:
            raise HTTPException(status_code=404, detail="Candidate not found")
        await self.candidate_repository.delete_candidate(id)

    async def get_all_candidates(self) -> List[Candidate]:
        return await self.candidate_repository.get_all_candidates()
