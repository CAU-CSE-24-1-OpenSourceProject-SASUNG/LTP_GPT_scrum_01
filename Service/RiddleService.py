from Init import *


class RiddleService:
    def __init__(self, session):
        self.session = session

    def create_riddle(self, id, hit_ratio):
        riddle = Riddle(id=id, hit_ratio=hit_ratio)
        self.session.add(riddle)
        self.session.commit()

    def get_riddle(self, riddle_id):
        return self.session.query(Riddle).filter_by(id=riddle_id).first()

    def get_all_riddle(self):
        return self.session.query(Riddle).all()

    def update_riddle(self, riddle_id, hit_ratio):
        riddle = self.get_riddle(riddle_id)
        if riddle:
            riddle.hit_ratio = hit_ratio
            self.session.commit()

    def delete_riddle(self, riddle_id):
        riddle = self.get_riddle(riddle_id)
        if riddle:
            games = self.session.query(Game).filter_by(riddle_id=riddle.id).all()
            if games:
                for game in games:
                    user_game = self.session.query(User_Game).filter_by(game_id=game.game_id).first()
                    if user_game:
                        self.session.delete(user_game)
                    self.session.delete(game)

            self.session.delete(riddle)
            self.session.commit()
