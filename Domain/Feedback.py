from Init import *

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(String(255), ForeignKey('queries.id'), primary_key=True)
    content = Column(String(255))

    query = relationship("Query", back_populates="feedback")