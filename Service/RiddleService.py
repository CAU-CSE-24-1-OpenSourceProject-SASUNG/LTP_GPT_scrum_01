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

    def delete_riddle(self, riddle_id):
        riddle = self.get_riddle(riddle_id)
        if riddle:
            games = self.session.query(Game).filter_by(riddle_id=riddle.id).all()
            if games:
                for game in games:
                    user_games = self.session.query(User_Game).filter_by(game_id=game.game_id).all()
                    if user_games:
                        for user_game in user_games:
                            self.session.delete(user_game)
                    self.session.delete(game)

            self.session.delete(riddle)
            self.session.commit()
