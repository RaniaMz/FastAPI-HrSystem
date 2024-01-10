# app/repositories/candidate_repository.py

from app.models.candidate import Candidate
from typing import List
from uuid import UUID


class CandidateRepository:
    candidates: List[Candidate] = []

    def create_candidate(self, candidate: Candidate):
        self.candidates.append(candidate)

    def get_candidate(self, uuid: UUID) -> Candidate:
        for candidate in self.candidates:
            if candidate.uuid == uuid:
                return candidate
        return None

    def update_candidate(self, uuid: UUID, updated_candidate: Candidate):
        for i, candidate in enumerate(self.candidates):
            if candidate.uuid == uuid:
                self.candidates[i] = updated_candidate
                return

    def delete_candidate(self, uuid: UUID):
        self.candidates = [candidate for candidate in self.candidates if candidate.uuid != uuid]

    def get_all_candidates(self) -> List[Candidate]:
        return self.candidates
