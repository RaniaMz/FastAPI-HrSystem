import os
import csv
from typing import List
from app.models.candidate import Candidate


def generate_csv_report(candidates: List[Candidate]) -> str:
    """
    Generate a CSV report of candidates' information.

    Args:
        candidates (List[Candidate]): List of candidates.

    Returns:
        str: File path of the generated CSV report.
    """
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    report_filename = "candidates_report.csv"
    report_file_path = os.path.join(report_dir, report_filename)

    with open(report_file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        header = [
            "First Name", "Last Name", "Email", "UUID", "Career Level", "Job Major",
            "Years of Experience", "Degree Type", "Skills", "Nationality", "City",
            "Salary", "Gender"
        ]
        writer.writerow(header)

        for candidate in candidates:
            row = [
                candidate.first_name, candidate.last_name, candidate.email,
                str(candidate.uuid), candidate.career_level, candidate.job_major,
                str(candidate.years_of_experience), candidate.degree_type,
                ", ".join(candidate.skills), candidate.nationality, candidate.city,
                str(candidate.salary), ", ".join(candidate.gender)
            ]
            writer.writerow(row)

    return report_file_path
