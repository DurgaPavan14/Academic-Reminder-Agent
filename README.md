# Academic Reminder Agent

## 📌 Overview
The **Academic Reminder Agent** is an action-enabled AI assistant powered by OpenAI's function calling. It accepts user prompts like:

> "Remind me to submit my AI assignment on Friday and email my advisor."

The agent interprets the message and performs two real-world tasks:
- Creates a calendar event
- Sends an automated email to the advisor

## 🧠 Features
- Natural language understanding via OpenAI GPT-4
- Modular Python functions for email, calendar, and storage
- Logs all actions in a JSON file
- Easily extensible (Trello, Slack, DB integration, etc.)

## 🛠️ Technologies
- Python 3
- OpenAI GPT-4 (function calling)
- JSON for local logging
- Modular file structure for scalability

## 🗂️ Project Structure
```
academic_reminder_agent/
├── main.py
├── agent_functions/
│   ├── calendar.py
│   ├── email.py
│   ├── storage.py
├── config/
│   └── settings.py
├── logs/
│   └── reminders_log.json
├── requirements.txt
├── README.md
└── architecture.png
```

## 🚀 How to Run
```bash
# Activate your virtual environment
venv\Scripts\activate     # Windows
source venv/bin/activate    # macOS/Linux

# Install required packages
pip install -r requirements.txt

# Add your OpenAI key in config/settings.py

# Run the agent
python main.py
```

## 🔍 Example Log
```json
[
  {
    "timestamp": "2025-07-08T15:32:00Z",
    "user_input": "Remind me to submit my AI assignment on Friday and email my advisor.",
    "function": "send_email_notification",
    "parameters": {
      "to": "advisor@example.com",
      "subject": "Assignment Reminder",
      "body": "Please note I will be submitting the assignment on Friday."
    }
  }
]
```

## 🧩 Extensibility Ideas
- Add Google Calendar or Microsoft Graph API
- Integrate with Slack or Trello
- Create a Streamlit UI
- Use SQLite or Firebase for persistent logging

## 📍 Author
Created by a Master's student in Computer Information Sciences as part of an AI agent systems course.
