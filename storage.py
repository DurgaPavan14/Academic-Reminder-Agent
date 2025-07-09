"""
Logs reminders and function calls to JSON file for traceability
"""
import json
from datetime import datetime

LOG_FILE = "logs/reminders_log.json"

def store_reminder_data(user_input, function_name, arguments):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_input": user_input,
        "function": function_name,
        "parameters": arguments
    }
    try:
        with open(LOG_FILE, 'r+') as file:
            data = json.load(file)
            data.append(log_entry)
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open(LOG_FILE, 'w') as file:
            json.dump([log_entry], file, indent=4)
