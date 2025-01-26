from fastapi import FastAPI, WebSocket
from app.chatbot import BankChatbot

import json
import os

app = FastAPI()


# Load the chatbot model
try:
    chatbot = BankChatbot.load_model()
except Exception as e:
    print(f"Error loading model: {e}")
    raise

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            response = chatbot.get_answer(data)
            await websocket.send_json({
                "question": data,
                "answer": response
            })
    except Exception as e:
        print(f"WebSocket Error: {e}")
    finally:
        await websocket.close()

@app.get("/")
def read_root():
    return {"message": "Bank Chatbot API is running!"}