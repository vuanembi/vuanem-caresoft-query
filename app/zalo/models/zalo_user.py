from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database.base import Base


class ZaloUser(Base):
    __tablename__ = "zalo_user"

    id = Column(Integer, primary_key=True, autoincrement="auto")

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    deleted_at = Column(DateTime(timezone=True))

    user_id = Column(String(), unique=True, nullable=False)

    phone = Column(String(), unique=True, nullable=False)
