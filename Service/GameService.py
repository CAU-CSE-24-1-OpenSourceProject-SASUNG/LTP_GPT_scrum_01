from Init import *


class GameService:
    def __init__(self, session):
        self.session = session

    def create_game(self, user_id, game_id, riddle_id, query_count, play_time, query_length, hit):
        game = Game(game_id=game_id, riddle_id=riddle_id, query_count=query_count, play_time=play_time,
                    query_length=query_length, hit=hit)
        user_game = User_Game(user_id=user_id, game_id=game_id)

        self.session.add(game)
        self.session.add(user_game)
        self.session.commit()

    def get_game(self, game_id):
        return self.session.query(Game).filter_by(game_id=game_id).first()

    def get_all_game(self):
        return self.session.query(Game)

    def delete_game(self, game_id):
        game = self.get_game(game_id)
        if game:
            user_games = self.session.query(User_Game).filter_by(game_id=game.game_id).all()
            if user_games:
                for user_game in user_games:
                    self.session.delete(user_game)

            self.session.delete(game)
            self.session.commit()
