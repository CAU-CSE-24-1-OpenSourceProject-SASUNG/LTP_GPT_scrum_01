from sqlalchemy import Column, String, ForeignKey, Integer, Time, Boolean
from sqlalchemy.orm import relationship

from src.Init import Base

class Game(Base):
    __tablename__ = 'games'

    game_id = Column(String(255), primary_key=True)
    riddle_id = Column(String(255), ForeignKey('riddles.riddle_id'))
    query_count = Column(Integer)
    play_time = Column(Time)
    query_length = Column(Integer)
    hit = Column(Boolean)

    game_queries = relationship("Game_Query")
    user_game = relationship('User_Game', uselist=False)
    riddle = relationship("Riddle", back_populates="games")