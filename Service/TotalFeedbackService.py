from Init import *


class TotalFeedbackService:
    def __init__(self, session):
        self.session = session

    def create_totalFeedback(self, user_id, content):
        total_feedback = Total_Feedback(id=user_id, content=content)
        self.session.add(total_feedback)
        self.session.commit()

    def get_totalFeedback(self, user_id):
        return self.session.query(Total_Feedback).filter_by(id=user_id).first()

    def get_all_totalFeedback(self):
        return self.session.query(Total_Feedback).all()

    def delete_totalFeedback(self, user_id):
        total_feedbacks = self.get_totalFeedback(user_id)
        if total_feedbacks:
            self.session.delete(total_feedbacks)
            self.session.commit()
