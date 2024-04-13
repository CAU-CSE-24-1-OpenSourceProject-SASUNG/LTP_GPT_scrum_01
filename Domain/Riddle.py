from sqlalchemy import Float

from alchemyTest import *

class Riddle(Base):
    __tablename__ = 'riddles'

    id = Column(String(255), primary_key=True)
    hit_ratio = Column(Float)

    games = relationship("Game")