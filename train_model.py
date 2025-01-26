from app.chatbot import BankChatbot

if __name__ == '__main__':
    print("Training chatbot model...")
    chatbot = BankChatbot()
    chatbot.save_model()
    print("Model training completed and saved!")