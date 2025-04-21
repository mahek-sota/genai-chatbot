# Replace with Redis/DB later
session_store = {}

def get_conversation(session_id: str):
    return session_store.get(session_id, [{"role": "system", "content": "You are a helpful assistant."}])

def add_to_conversation(session_id: str, conversation: list):
    session_store[session_id] = conversation
