from sqlalchemy import Column, String, ForeignKey
from src.Init import Base

class User_Game(Base):
    __tablename__ = 'user_games'

    user_id = Column(String(255), ForeignKey('users.user_id'), primary_key=True)
    game_id = Column(String(255), ForeignKey('games.game_id'), primary_key=True)