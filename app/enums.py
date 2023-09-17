from enum import Enum


class Role(Enum):
    """
    Enum representing participant roles in a conversation.
    - `SYSTEM`: Represents the system or initialization role.
    - `USER`: Represents the user's role in the conversation.
    - `ASSISTANT`: Represents the conversational assistant's role.
    """
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
