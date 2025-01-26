# AskiniBot 🤖

A smart banking FAQ chatbot powered by Python NLP and React.js. Get instant answers to common banking queries through a friendly web interface.

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Node.js 18+](https://img.shields.io/badge/node.js-18+-green.svg)](https://nodejs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103.2-lightgreen.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2.0-blue.svg)](https://reactjs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Chatbot Demo](./path/to/demo-gif.gif) <!-- Add your demo gif/image here -->

## Features ✨
- Real-time WebSocket communication
- Natural Language Processing (NLP) for question matching
- Modern React UI with animations
- Responsive design for all devices
- Easy-to-extend FAQ knowledge base
- Virtual environment support
- Docker deployment ready

## Prerequisites 📋
- Python 3.10+
- Node.js 18+
- npm/yarn
- Git

## Project Structure 📂
bank-chatbot/
├── app/ # Backend API
│ ├── init.py
│ ├── chatbot.py # NLP processing
│ ├── main.py # FastAPI server
│ └── models/ # Trained models (ignored)
├── client/ # Frontend React app
├── data/ # Training data (ignored)
├── venv/ # Python virtual env (ignored)
├── .gitignore
├── requirements.txt # Python dependencies
├── train_model.py # Model training script
└── README.md

## Setup & Installation 🛠️

### 1. Clone Repository
```bash
git clone https://github.com/Houssem-DH/AskiniBot.git
cd bank-chatbot

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python train_model.py

uvicorn app.main:app --reload --host 0.0.0.0 --port 3500 bash```

