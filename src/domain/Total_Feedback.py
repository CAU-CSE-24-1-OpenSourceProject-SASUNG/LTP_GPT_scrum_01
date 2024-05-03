from sqlalchemy import Column, String, ForeignKey

from src.Init import Base

class Total_Feedback(Base):
    __tablename__ = "total_feedbacks"

    user_id = Column(String(255), ForeignKey('users.user_id'), primary_key=True)
    content = Column(String(255))