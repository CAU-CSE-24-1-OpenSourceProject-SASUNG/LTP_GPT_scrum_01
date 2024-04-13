from Init import *


class Total_Feedback(Base):
    __tablename__ = "total_feedbacks"

    id = Column(String(255), ForeignKey('user_games.user_id'), primary_key=True)
    content = Column(String(255))

    user = relationship("User", back_populates="total_feedback")