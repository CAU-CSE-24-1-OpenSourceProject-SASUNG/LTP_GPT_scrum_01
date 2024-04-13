import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import relationship, sessionmaker

# db연결 및 객체 베이스 생성
engine = create_engine('mysql+pymysql://root:gusdn4818@localhost/ossp', echo=True)
Base = sqlalchemy.orm.declarative_base()

# Session 선언. Session을 이용하여 db를 조작 가능
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(String(255), primary_key=True)
    email = Column(String(255))

    user_games = relationship("User_Game")
    total_feedback = relationship("Total_Feedback", uselist=False, back_populates='user')


class User_Game(Base):
    __tablename__ = 'user_games'

    user_id = Column(String(255), ForeignKey('users.user_id'), primary_key=True)
    game_id = Column(String(255), ForeignKey('games.game_id'), primary_key=True)

    game = relationship('Game', back_populates='user_game')


class Total_Feedback(Base):
    __tablename__ = "total_feedbacks"

    id = Column(String(255), ForeignKey('users.user_id'), primary_key=True)
    content = Column(String(255))

    user = relationship("User", back_populates="total_feedback")


class Riddle(Base):
    __tablename__ = 'riddles'

    id = Column(String(255), primary_key=True)
    hit_ratio = Column(Float)

    games = relationship("Game")


class Query(Base):
    __tablename__ = "queries"

    id = Column(String(255), primary_key=True)
    query = Column(String(255))
    response = Column(String(255))
    is_correct = Column(Boolean)

    game_query = relationship('Game_Query', uselist=False, back_populates='query')
    feedback = relationship('Feedback', uselist=False, back_populates='query')


class Game_Query(Base):
    __tablename__ = "game_queries"

    game_id = Column(String(255), ForeignKey('games.game_id'), primary_key=True)
    query_id = Column(String(255), ForeignKey('queries.id'), primary_key=True)

    query = relationship('Query', back_populates='game_query')


class Game(Base):
    __tablename__ = 'games'

    game_id = Column(String(255), primary_key=True)
    riddle_id = Column(String(255), ForeignKey('riddles.id'))
    query_count = Column(Integer)
    play_time = Column(Time)
    query_length = Column(Integer)
    hit = Column(Boolean)

    game_queries = relationship("Game_Query")
    user_game = relationship('User_Game', uselist=False, back_populates='game')


class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(String(255), ForeignKey('queries.id'), primary_key=True)
    content = Column(String(255))

    query = relationship("Query", back_populates="feedback")


Base.metadata.create_all(engine)

# insert
'''
user = User(id = 22222, name='zeo', email='zeo@example.com')
session.add(user)
user2 = User(id = 33333, name='potato', email='potato@example.com')
session.add(user2)
session.commit() #db를 write하는 경우는 commit을 해줘야 실제 db에 반영이 됨
'''

# #조회
# Johns = session.query(User).filter_by(name='John').all()
#
# print("------")
# for john in Johns :
#     print(john.id, john.name, john.email)
# print("------")
'''
#update
user = session.query(User).filter_by(name='potato').first()
user.name = 'kyu'
session.commit()
'''

# delete
'''
user = session.query(User).filter_by(name='zeo').first()
session.delete(user)
session.commit()
#session.query(User).filter_by(name='John').delete() #이렇게 바로 사용도 가능하다
'''
