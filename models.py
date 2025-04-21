from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id: str
    user_input: str

class ChatResponse(BaseModel):
    bot_reply: str
