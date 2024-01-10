# app/api/candidate.py
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query

from ..api.dependencies import get_current_user
from ..models.candidate import Candidate
from ..models.user import User
from ..services import user_service
from ..services.candidate_service import CandidateService
from ..utils.csv_generator import generate_csv_report

from app.repositories.candidate_repository import CandidateRepository
from typing import List

router = APIRouter()


@router.get("/all-candidates")
def get_all_candidates(
        keyword: str = Query(None, description="Search keyword for global search"),
        candidate_service: CandidateService = Depends(CandidateService)
):
    if keyword:
        # Perform global search based on the keyword
        matched_candidates = candidate_service.global_search(keyword)
    else:
        # If no keyword, get all candidates
        matched_candidates = candidate_service.get_all_candidates()

    return matched_candidates


@router.get("/generate-report")
def generate_report(
        candidate_service: CandidateService = Depends(CandidateService)
):
    candidates = candidate_service.get_all_candidates()

    if not candidates:
        raise HTTPException(status_code=404, detail="No candidates found to generate a report")

    # Generate CSV report and return the file path
    report_file_path = generate_csv_report(candidates)
    return {"message": "Report generated successfully", "report_file_path": report_file_path}


@router.post("/candidate")
def create_candidate(candidate: Candidate, candidate_service: CandidateService = Depends(CandidateService)):
    candidate_service.create_candidate(candidate)
    return {"message": "Candidate created successfully"}


@router.get("/candidate/{uuid}")
def get_candidate(uuid: UUID, candidate_service: CandidateService = Depends(CandidateService)):
    return candidate_service.get_candidate(uuid)


@router.get("/candidate/{uuid}", response_model=Candidate)
def get_candidate(
        uuid: UUID,
        current_user: User = Depends(get_current_user),
        candidate_service: CandidateService = Depends(CandidateService)
):
    # Check if the current user is authorized to access the candidate
    if not user_service.is_user_authorized(current_user, uuid):
        raise HTTPException(status_code=403, detail="User not authorized to access this candidate")

    return candidate_service.get_candidate(uuid)


@router.get("/all-candidates", response_model=List[Candidate])
def get_all_candidates(
        current_user: User = Depends(get_current_user),
        candidate_service: CandidateService = Depends(CandidateService)
):
    # Check if the current user is authorized to access all candidates
    if not user_service.is_user_authorized_all_candidates(current_user):
        raise HTTPException(status_code=403, detail="User not authorized to access all candidates")

    return candidate_service.get_all_candidates()


@router.put("/candidate/{uuid}")
def update_candidate(uuid: UUID, updated_candidate: Candidate,
                           candidate_service: CandidateService = Depends(CandidateService)):
    candidate_service.update_candidate(uuid, updated_candidate)
    return {"message": "Candidate updated successfully"}


@router.delete("/candidate/{uuid}")
def delete_candidate(uuid: UUID, candidate_service: CandidateService = Depends(CandidateService)):
    candidate_service.delete_candidate(uuid)
    return {"message": "Candidate deleted successfully"}


@router.get("/candidates")
def get_all_candidates(candidate_service: CandidateService = Depends(CandidateService)):
    return candidate_service.get_all_candidates()
