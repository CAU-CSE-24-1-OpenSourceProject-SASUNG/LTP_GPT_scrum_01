from Init import *

class Game_Query(Base):
    __tablename__ = "game_queries"

    game_id = Column(String(255), ForeignKey('games.id'), primary_key=True)
    query_id = Column(String(255), ForeignKey('queries.id'), primary_key=True)

    query = relationship('Query', back_populates='game_query')
