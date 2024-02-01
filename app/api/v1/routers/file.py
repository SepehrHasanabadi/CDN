from pathlib import Path
from ..crud.user import get_user_by_username

from app.database.session import get_db
from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.orm import Session

from app.services.file_manager import FileManager
from ..crud.file import update_or_create_file_in_db, get_all_user_file
from ..dependencies import verify_token
from ..schemas.file import File as FileSchema
from app.core.config import Settings

settings = Settings()

router = APIRouter()


@router.post("/cache-file/")
async def create_cache_file(
    file: UploadFile = File(...),
    minify: bool = Form(False),
    username: str = Depends(verify_token),
    db: Session = Depends(get_db),
):
    upload_dir = Path(f"{settings.upload_base_file}{username}")
    upload_dir.mkdir(parents=True, exist_ok=True)
    file_path = upload_dir / file.filename
    manager = FileManager(file)
    try:
        manager.save_file(file_path, minify)
    except ValueError as e:
        return {"error": str(e)}
    file_size = manager.get_file_size()
    file_format = manager.get_file_format()
    minify_duration = manager.get_file_minify_duration()
    memory_usage = manager.get_file_minify_memory_usage()
    user = get_user_by_username(db=db, username=username)
    uploaded_filed = update_or_create_file_in_db(
        db,
        memory_usage=memory_usage,
        minify_duration=minify_duration,
        size=file_size,
        path=str(file_path),
        type=file_format,
        user_id=user.id,
    )

    upload_file_response = FileSchema(
        size=uploaded_filed.size,
        type=uploaded_filed.type,
        minify_duration=uploaded_filed.minify_duration,
        minify_ram_consumption=uploaded_filed.minify_ram_consumption,
        created_at=uploaded_filed.created_at,
    )
    return upload_file_response


@router.get("/cache-file/")
async def create_cache_file(
    username: str = Depends(verify_token),
    db: Session = Depends(get_db),
):
    files = get_all_user_file(db, username)
    file_list = [
        FileSchema(
            size=file.size,
            type=file.type,
            minify_duration=file.minify_duration,
            minify_ram_consumption=file.minify_ram_consumption,
            created_at=file.created_at,
        )
        for file in files
    ]

    return file_list
