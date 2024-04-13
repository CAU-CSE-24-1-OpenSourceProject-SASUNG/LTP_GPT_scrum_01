from sqlalchemy import false

from Init import *


class User(Base):
    __tablename__ = 'users'

    id = Column(String(255), primary_key=True)
    email = Column(String(255))

    user_games = relationship("User_Game")
    total_feedback = relationship("Total_Feedback", uselist=false, back_populates='user')

# uselist : true면 일대다 / 다대다 관계, false면 일대일 관계
# back_populates : 양방향 관계 설정
# user - user_game : 일대다 : -> 단방향
# user - total_feedback : 일대일 : -> 단방향
# user_game - game : 일대일 :
# game - game_query : 일대다
# game_query - query : 일대일
# game - riddle : 다대일
# query - feedback : 일대일
