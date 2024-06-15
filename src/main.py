import uuid
import ltp_gpt

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from Init import session
from Init import engine
from Service.UserService import UserService
from Service.GameService import GameService
from Service.QueryService import QueryService
from Service.RiddleService import RiddleService
from Service.FeedbackService import FeedbackService
from Service.TotalFeedbackService import TotalFeedbackService
from sqlalchemy import text

app = FastAPI()
templates = Jinja2Templates(directory="templates")

userService = UserService(session)
gameService = GameService(session)
riddleService = RiddleService(session)
queryService = QueryService(session)
feedbackService = FeedbackService(session)
totalFeedbackService = TotalFeedbackService(session)

# DB 모든 데이터 삭제
with engine.connect() as conn:
    table_names = ['user_games', 'total_feedbacks', 'users', 'game_queries', 'games', 'riddles', 'feedbacks', 'queries']
    conn.execute(text('SET FOREIGN_KEY_CHECKS = 0;'))  # 외래 키 제약 조건을 잠시 해제
    for table_name in table_names:
        delete_query = text('TRUNCATE TABLE {};'.format(table_name))
        conn.execute(delete_query)
    conn.execute(text('SET FOREIGN_KEY_CHECKS = 1;'))  # 외래 키 제약 조건을 다시 활성화


# 게임 시작 초기 DB 설정

# 로그인
user_id = str(uuid.uuid4())
userService.create_user(user_id, 'tlsgusdn4818@gmail.com')

# 게임의 종류를 선택
riddleService.create_riddle('Umbrella', 0)
game_id = str(uuid.uuid4())
gameService.create_game(user_id, game_id, 'Umbrella', 0, 0, 0, False)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    problem = "어떤 아이가 아파트 10층에 살고 있으며, 맑은 날에는 엘리베이터에서 6층에서 내려서 10층까지 걸어 올라간다. 그러나 날씨가 좋지 않다면 10층에서 내려서 집으로 간다. 어떤 상황일까?"
    return templates.TemplateResponse("index.html", {"request": request, "problem": problem})


@app.post("/chat")
async def chat(request: Request):
    try:
        body = await request.json()
        question = body.get("question")
        response = ltp_gpt.evaluate_question(question)
        query_id = str(uuid.uuid4())
        queryService.create_query(game_id, query_id, question, response, False)
        return JSONResponse(content={"response": response})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
