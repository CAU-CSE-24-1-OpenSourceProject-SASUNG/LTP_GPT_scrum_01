from sqlalchemy import Boolean, Time, false

from Init import *

class Game(Base):
    __tablename__ = 'games'

    id = Column(String(255), primary_key=True)
    riddle_id = Column(String(255), ForeignKey('riddles.id'))
    query_count = Column(Integer)
    play_time = Column(Time)
    query_length = Column(Integer)
    hit = Column(Boolean)

    game_queries = relationship("Game_Query")
    user_game = relationship('Game', uselist=false, back_populates='game')



