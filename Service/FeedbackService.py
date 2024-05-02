from Init import *


class FeedbackService:
    def __init__(self, session):
        self.session = session

    def create_feedback(self, query_id, content):
        feedback = Feedback(query_id=query_id, content=content)

        self.session.add(feedback)
        self.session.commit()

    def get_feedback(self, query_id):
        return self.session.query(Feedback).filter_by(query_id=query_id).first()

    def get_all_feedback(self):
        return self.session.query(Feedback).all()

    def delete_feedback(self, query_id):
        feedback = self.get_feedback(query_id)
        if feedback:
            self.session.delete(feedback)
            self.session.commit()
