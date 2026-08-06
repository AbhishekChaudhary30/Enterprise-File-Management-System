from pathlib import Path

from fastapi import APIRouter
from fastapi import HTTPException

from efms.services.scan_service import ScanService

router = APIRouter()

scan_service = ScanService()


@router.get("/health")
def health():

    return {

        "status": "ok",

        "application": "Enterprise File Management System",

    }


@router.get("/scan")
def scan(path: str):

    directory = Path(path)

    if not directory.exists():

        raise HTTPException(

            status_code=404,

            detail="Directory not found",

        )

    return scan_service.scan(directory)