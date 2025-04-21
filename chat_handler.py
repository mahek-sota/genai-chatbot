from openai import ChatCompletion
from memory_store import get_conversation, add_to_conversation
from config import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

async def handle_chat(session_id: str, user_input: str) -> str:
    history = get_conversation(session_id)
    history.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=history,
        temperature=0.7,
        max_tokens=300
    )

    bot_reply = response["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": bot_reply})
    add_to_conversation(session_id, history)

    return bot_reply
