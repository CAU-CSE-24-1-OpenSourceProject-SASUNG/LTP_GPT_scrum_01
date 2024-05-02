from Init import *


class QueryService:
    def __init__(self, session):
        self.session = session

    def create_query(self, game_id, query_id, query, response, is_correct):
        query = Query(query_id=query_id, query=query, response=response, is_correct=is_correct)
        game_query = Game_Query(game_id=game_id, query_id=query_id)

        self.session.add(query)
        self.session.add(game_query)
        self.session.commit()

    def get_query(self, query_id):
        return self.session.query(Query).filter_by(query_id=query_id).first()

    def get_all_query(self):
        return self.session.query(Query).all()

    def delete_query(self, query_id):
        query = self.get_query(query_id)
        if query:
            game_query = self.session.query(Game_Query).filter_by(query_id=query_id).first()
            feedback = self.session.query(Feedback).filter_by(query_id=query_id).first()

            if game_query:
                self.session.delete(game_query)
            if feedback:
                self.session.delete(feedback)

            self.session.delete(query)
            self.session.commit()
