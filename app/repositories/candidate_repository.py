from typing import List

from bson import ObjectId
from fastapi import HTTPException
from starlette import status

from app.db.mongodb import db
from app.models.candidate import Candidate, UpdateCandidate


class CandidateRepository:
    async def create_candidate(self, candidate: Candidate) -> Candidate:
        candidate_collection = db.client.get_database().get_collection('candidates')

        result = await candidate_collection.insert_one(candidate.model_dump())

        inserted_candidate = await candidate_collection.find_one({
            "_id": result.inserted_id
        })
        return inserted_candidate

    async def get_candidate(self, id: str) -> Candidate:
        candidate_collection = db.client.get_database().get_collection('candidates')

        try:
            candidate_id = ObjectId(id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid candidate ID format: {e}"
            )

        candidate = await candidate_collection.find_one({
            "_id": candidate_id
        })

        if candidate:
            return candidate

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Candidate with ID {id} not found"
        )

    async def update_candidate(self, id: str, updated_candidate: UpdateCandidate) -> UpdateCandidate:
        candidate_collection = db.client.get_database().get_collection('candidates')

        try:
            candidate_id = ObjectId(id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid candidate ID format: {e}"
            )

        result = await candidate_collection.update_one(
            {"_id": candidate_id},
            {"$set": updated_candidate.model_dump(exclude_unset=True)}
        )

        updated_candidate = await candidate_collection.find_one({"_id": candidate_id})

        if updated_candidate:
            return updated_candidate

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {id} not found"
        )

    async def delete_candidate(self, id: str):
        candidate_collection = db.client.get_database().get_collection('candidates')

        try:
            candidate_id = ObjectId(id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid candidate ID format: {e}"
            )

        await candidate_collection.delete_one({
            "_id": candidate_id
        })

    async def get_all_candidates(self):
        candidates: List[Candidate] = []

        candidate_collection = db.client.get_database().get_collection('candidates')

        cursor = candidate_collection.find({})
        async for row in cursor:
            print(row)
            candidates.append(Candidate(**row))

        return candidates
