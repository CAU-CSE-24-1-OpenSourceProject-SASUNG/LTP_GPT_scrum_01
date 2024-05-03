from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship

from src.Init import Base

class Riddle(Base):
    __tablename__ = 'riddles'

    riddle_id = Column(String(255), primary_key=True)
    hit_ratio = Column(Float)

    games = relationship("Game", back_populates="riddle")