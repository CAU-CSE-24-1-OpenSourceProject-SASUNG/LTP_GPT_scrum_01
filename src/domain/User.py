from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.Init import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(String(255), primary_key=True)
    email = Column(String(255))

    user_games = relationship("User_Game")
    total_feedback = relationship("Total_Feedback", uselist=False)
