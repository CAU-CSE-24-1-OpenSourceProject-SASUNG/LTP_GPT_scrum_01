from sqlalchemy import Boolean, false

from Init import *


class Query(Base):
    __tablename__ = "queries"

    id = Column(String(255), primary_key=True)
    query = Column(String(255))
    response = Column(String(255))
    feedback = Column(Boolean)

    game_query = relationship('Game_Query', uselist=false, back_populates='query')
    feedback = relationship('Feedback', uselist=false, back_populates='query')
