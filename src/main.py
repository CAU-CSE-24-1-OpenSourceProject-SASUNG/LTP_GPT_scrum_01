from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import ltp_gpt

app = FastAPI()
templates = Jinja2Templates(directory="templates")

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
        if response != "아닙니다." and response != "문제의 정답과 상관이 없습니다." and response != "맞습니다." and response != "그렇다고 볼 수도 있습니다." and response != "정확한 정답을 맞추셨습니다." and response != "정답과 유사합니다." and response != "모르겠습니다":
            response = "직접적인 질문에 대답해 드릴 수 없습니다"
        return JSONResponse(content={"response": response})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

