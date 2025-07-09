"""
Main entry point for the Academic Reminder Agent
Handles user input and dispatches actions using OpenAI function calling
"""

from agent_functions.calendar import create_calendar_event
from agent_functions.email import send_email_notification
from agent_functions.storage import store_reminder_data
from config.settings import CONFIG
import json
import openai

# Sample user message
user_input = "Remind me to submit my AI assignment on Friday and email my advisor."

# Define OpenAI function schemas
function_schemas = [
    {
        "name": "create_calendar_event",
        "description": "Creates a calendar event based on extracted details",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "date": {"type": "string", "format": "date"}
            },
            "required": ["title", "date"]
        }
    },
    {
        "name": "send_email_notification",
        "description": "Sends an email to the advisor with reminder",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {"type": "string"},
                "subject": {"type": "string"},
                "body": {"type": "string"}
            },
            "required": ["to", "subject", "body"]
        }
    }
]

# Setup OpenAI client
openai.api_key = CONFIG['openai_api_key']

# Call OpenAI ChatCompletion with function calling
response = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages=[{"role": "user", "content": user_input}],
    functions=function_schemas,
    function_call="auto"
)

# Get the function call result
message = response["choices"][0]["message"]
if "function_call" in message:
    function_name = message["function_call"]["name"]
    arguments = json.loads(message["function_call"]["arguments"])

    # Dispatch function
    if function_name == "create_calendar_event":
        create_calendar_event(arguments["title"], arguments["date"])
    elif function_name == "send_email_notification":
        send_email_notification(arguments["to"], arguments["subject"], arguments["body"])

    # Store the interaction log
    store_reminder_data(user_input, function_name, arguments)
else:
    print("No function call triggered.")
