import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

#db연결 및 객체 베이스 생성
engine = create_engine('mysql://root:andandtlqk1!@localhost/osp', echo=True)
Base = sqlalchemy.orm.declarative_base()

#테이블과 매칭될 객체 선언. tablename이 반드시 db내에 이미 존재하는 테이블의 이름이어야함. PK 조건도 같아야만 함. 변수 이름은 상관 없음
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

#Session 선언. Session을 이용하여 db를 조작 가능
Session = sessionmaker(bind=engine)
session = Session()

#insert
'''
user = User(id = 22222, name='zeo', email='zeo@example.com')
session.add(user)
user2 = User(id = 33333, name='potato', email='potato@example.com')
session.add(user2)
session.commit() #db를 write하는 경우는 commit을 해줘야 실제 db에 반영이 됨
'''

#조회
Johns = session.query(User).filter_by(name='John').all()

print("------")
for john in Johns :
    print(john.id, john.name, john.email)
print("------")
'''
#update
user = session.query(User).filter_by(name='potato').first()
user.name = 'kyu'
session.commit()
'''

#delete
'''
user = session.query(User).filter_by(name='zeo').first()
session.delete(user)
session.commit()
#session.query(User).filter_by(name='John').delete() #이렇게 바로 사용도 가능하다
'''



