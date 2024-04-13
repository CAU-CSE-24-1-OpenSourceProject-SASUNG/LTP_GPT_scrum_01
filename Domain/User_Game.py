from alchemyTest import *

class User_Game(Base):
    __tablename__ = 'user_games'

    user_id = Column(String(255), ForeignKey('users.id'), primary_key=True)
    game_id = Column(String(255), ForeignKey('games.id'), primary_key=True)

    game = relationship('Game', back_populates='user_game')