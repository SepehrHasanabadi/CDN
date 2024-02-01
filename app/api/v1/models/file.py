from app.database.base import Base
from sqlalchemy import ForeignKey, Column, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, nullable=False)
    path = Column(String, index=True, nullable=False)
    size = Column(String, nullable=False)
    type = Column(String, nullable=False)
    minify_duration = Column(String, nullable=True)
    minify_ram_consumption = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

    user = relationship("User", back_populates="files")
