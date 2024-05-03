from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.Init import Base

class Feedback(Base):
    __tablename__ = "feedbacks"

    query_id = Column(String(255), ForeignKey('queries.query_id'), primary_key=True)
    content = Column(String(255))

    query = relationship("Query", uselist=False, back_populates="feedback")