from sqlalchemy import Column, String, ForeignKey

from src.Init import Base


class Game_Query(Base):
    __tablename__ = "game_queries"

    game_id = Column(String(255), ForeignKey('games.game_id'), primary_key=True)
    query_id = Column(String(255), ForeignKey('queries.query_id'), primary_key=True)