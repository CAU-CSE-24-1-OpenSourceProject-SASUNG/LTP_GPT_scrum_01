from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from src.Init import Base

class Query(Base):
    __tablename__ = "queries"

    query_id = Column(String(255), primary_key=True)
    query = Column(String(255))
    response = Column(String(255))
    is_correct = Column(Boolean)

    game_query = relationship('Game_Query', uselist=False)
    feedback = relationship('Feedback', uselist=False, back_populates='query')