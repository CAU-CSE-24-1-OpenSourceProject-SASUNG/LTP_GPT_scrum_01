from Init import session
from Service.UserService import UserService
from Service.GameService import GameService
from Service.RiddleService import RiddleService

userService = UserService(session)
gameService = GameService(session)
riddleService = RiddleService(session)

# userService.create_user(1, 'tlsgusdn4818@gmail.com')
# userService.create_user(2, 'spdlqj4818@cau.ac.kr')
# userService.delete_user(1)
# riddleService.create_riddle('Umbrella', 0.5)
# riddleService.create_riddle('Elevator', 0)

# gameService.create_game(1, 1, 'Umbrella', 20, 100, 500, True)
# gameService.delete_game(3)
# gameService.create_game(1, 2, 'Elevator', 10, 10, 100, True)
# gameService.create_game(2, 3, 'Umbrella', 10, 10, 100, False)
# gameService.create_game(2, 4, 'Elevator', 10,10,100,True)
# riddleService.delete_riddle('Elevator')

print('---사용자 목록---')
all_users = userService.get_all_user()
for user in all_users:
    print(user.user_id, user.email)

print('---게임 목록---')
all_games = gameService.get_all_game()
for game in all_games:
    print(game.game_id, game.riddle_id)

print('---게임 종류 목록---')
all_riddles = riddleService.get_all_riddle()
for riddle in all_riddles:
    print(riddle.id)