from Init import *


class GameService:
    def __init__(self, session):
        self.session = session

    def create_game(self, user_id, riddle_id, query_count, play_time, query_length, hit):
        game = Game(riddle_id=riddle_id, query_count=query_count, play_time=play_time,
                    query_length=query_length, hit=hit)
        self.session.add(game)
        self.session.flush()

        user_game = User_Game(user_id=user_id, game_id=game.game_id)
        self.session.add(user_game)
        self.session.commit()

    def get_game(self, game_id):
        return self.session.query(Game).filter_by(game_id=game_id).first()

    def get_all_game(self):
        return self.session.query(Game).all()

    def delete_game(self, game_id):
        game = self.get_game(game_id)
        if game:
            user_game = self.session.query(User_Game).filter_by(game_id=game.game_id).first()
            game_queries = self.session.query(Game_Query).filter_by(game_id=game.game_id).all()

            if user_game:
                self.session.delete(user_game)
            if game_queries:
                for game_query in game_queries:
                    self.session.delete(game_query)

            self.session.delete(game)
            self.session.commit()
