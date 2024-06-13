from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Query(Base):
    __tablename__ = "queries"

    id = Column(Integer, primary_key=True)
    prompt = Column(String, index=True)
    completion = Column(String, index=True)

