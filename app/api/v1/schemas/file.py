from datetime import datetime
from pydantic import BaseModel


class File(BaseModel):
    size: str
    minify_duration: str
    minify_ram_consumption: str
    type: str
    created_at: datetime
