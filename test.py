from Init import session
from Service.UserService import UserService
from Service.GameService import GameService
from Service.RiddleService import RiddleService
from Service.QueryService import QueryService
from Service.FeedbackService import FeedbackService
from Service.TotalFeedbackService import TotalFeedbackService

userService = UserService(session)
gameService = GameService(session)
riddleService = RiddleService(session)
queryService = QueryService(session)
feedbackService = FeedbackService(session)
totalFeedbackService = TotalFeedbackService(session)

# userService.create_user(1, 'tlsgusdn4818@gmail.com')
# userService.create_user(2, 'sihuny36@gmail.com')
# userService.create_user(3, 'rbt2775@cau.ac.kr')
# userService.create_user(4, 'wodh7223@cau.ac.kr')
#
# riddleService.create_riddle('Umbrella', 0)
# riddleService.create_riddle('Elevator', 0)
#
# gameService.create_game(1, 'Umbrella', 1, 1, 1, True)
# gameService.create_game(1, 'Elevator', 1, 1, 1, True)
# gameService.create_game(2, 'Umbrella', 1, 1, 1, True)
# gameService.create_game(2, 'Elevator', 1, 1, 1, True)
# gameService.create_game(3, 'Umbrella', 1, 1, 1, True)
# gameService.create_game(3, 'Elevator', 1, 1, 1, True)
# gameService.create_game(4, 'Umbrella', 1, 1, 1, True)
# gameService.create_game(4, 'Elevator', 1, 1, 1, True)
#
# totalFeedbackService.create_totalFeedback(1, 'Hello')
# totalFeedbackService.create_totalFeedback(2, 'Hi')
# totalFeedbackService.create_totalFeedback(3, 'Bye')
# totalFeedbackService.create_totalFeedback(4, 'Huh')

# queryService.create_query('333220b5-f6c3-401b-9353-c63f388c2a05', 'a', 'a', True)
# queryService.create_query('333220b5-f6c3-401b-9353-c63f388c2a05', 'b', 'b', True)
# queryService.create_query('7faa3ed7-b9b8-4ecc-b18a-594744aab138', 'c', 'c', False)

# feedbackService.create_feedback('0f12d530-5c13-4898-b871-d40e56dfb4eb', 'Good')
# queryService.delete_query('0f12d530-5c13-4898-b871-d40e56dfb4eb')

# feedbackService.create_feedback(1, 'Good')
# feedbackService.create_feedback(2, 'Bad')

# print('---사용자 목록---')
# all_users = userService.get_all_user()
# for user in all_users:
#     print(user.user_id, user.email)
#
# print('---게임 목록---')
# all_games = gameService.get_all_game()
# for game in all_games:
#     print(game.game_id, game.riddle_id)
#
# print('---게임 종류 목록---')
# all_riddles = riddleService.get_all_riddle()
# for riddle in all_riddles:
#     print(riddle.riddle_id)
