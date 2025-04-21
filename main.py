from fastapi import FastAPI, HTTPException
from models import ChatRequest, ChatResponse
from chat_handler import handle_chat

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    try:
        response = await handle_chat(req.session_id, req.user_input)
        return ChatResponse(bot_reply=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
