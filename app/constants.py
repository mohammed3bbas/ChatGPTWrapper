from app.enums import Role

# System prompt to set initial behavior
SYSTEM_PROMPT = {
    "role": Role.SYSTEM.value,
    "content": "You are a friendly and adaptable conversational partner. Strive to provide engaging and helpful responses while maintaining a warm and approachable tone throughout the conversation."
}
WELCOME_MESSAGE = "Welcome to Chat Assistant API Wrapper!"
ERROR_MISSING_MESSAGE = "Missing 'message' in request JSON"
ERROR_INVALID_JSON = "Invalid JSON format"
ERROR_UNSPORTED_MEDIA = "Unsupported Media Type"
ERROR_EMPTY_JSON = "Empty JSON request body"
ERROR_INVALID_COMPLETION_TYPE = "Invalid model completion type"
GPT_3_5_TURBO_MODEL = "gpt-3.5-turbo-0613"
CHAT_MODEL = 'gpt'
