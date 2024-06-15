from Init import session
from src.Service.UserService import UserService
from src.Service.GameService import GameService
from src.Service.RiddleService import RiddleService
from src.Service.QueryService import QueryService
from src.Service.FeedbackService import FeedbackService
from src.Service.TotalFeedbackService import TotalFeedbackService

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

# queryService.create_query('09bff8bd-a4dc-47dd-8da7-4be8698344a1', 'a', 'a', True)
# queryService.create_query('09bff8bd-a4dc-47dd-8da7-4be8698344a1', 'b', 'b', True)
# queryService.create_query('0a650417-8cef-4b6b-97da-8195e196b946', 'c', 'c', False)
# feedbackService.create_feedback('86ae97d3-2247-4d06-bea0-c8699570e714', 'Good')

# queryService.delete_query('86ae97d3-2247-4d06-bea0-c8699570e714')
# userService.delete_user(1)
# gameService.delete_game('09bff8bd-a4dc-47dd-8da7-4be8698344a1')
# riddleService.delete_riddle('Elevator')

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
