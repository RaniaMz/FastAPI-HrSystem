# src/api/candidate.py
from typing import List
from fastapi import APIRouter, HTTPException
from starlette import status
from fastapi.responses import FileResponse

from app.models.candidate import Candidate, UpdateCandidate
from app.services.candidate_service import CandidateService
from app.utils.csv_generator import generate_csv_report

router = APIRouter()


@router.post("/candidate",
             response_description='create candidate',
             status_code=status.HTTP_201_CREATED,
             response_model=Candidate,
             tags=['Candidate Section'])
async def create_candidate(candidate: Candidate):
    try:
        return await CandidateService().create_candidate(candidate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/candidate/{id}",
            response_model=Candidate,
            response_description='get candidate',
            status_code=status.HTTP_200_OK,
            tags=['Candidate Section'])
async def get_candidate(id: str):
    return await CandidateService().get_candidate(id)


@router.get("/all-candidates",
            response_model=List[Candidate],
            response_description='get all candidates',
            status_code=status.HTTP_200_OK,
            tags=['Candidate Section'])
async def get_all_candidates():
    return await CandidateService().get_all_candidates()


@router.put("/candidate/{id}",
            response_description='update candidate',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=Candidate,
            tags=['Candidate Section'])
async def update_candidate(id: str, updated_candidate: UpdateCandidate):
    try:
        return await CandidateService().update_candidate(id, updated_candidate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.delete("/candidate/{id}",
               response_description='delete candidate',
               status_code=status.HTTP_200_OK,
               response_model=str,
               tags=['Candidate Section'])
async def delete_candidate(id: str):
    try:
        await CandidateService().delete_candidate(id)
        return {"message": "Candidate deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/generate-report", response_description='generate report',
            status_code=status.HTTP_200_OK, tags=['Candidate Section'])
async def generate_report():

    candidates = await CandidateService().get_all_candidates()

    if not candidates:
        raise HTTPException(status_code=404, detail="No candidates found to generate a report")

    report_file_path = generate_csv_report(candidates)
    return FileResponse(report_file_path)
