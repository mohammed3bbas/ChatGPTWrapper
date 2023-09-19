from app.constants import ERROR_INVALID_COMPLETION_TYPE
from app.models.chat_completion import ChatCompletionBase, GPTChatCompletion


class ChatCompletionFactory:
    """
    A factory class for creating chat completion instances.

    This factory allows you to create instances of various chat completion systems
    based on the specified completion type. based on the need, you can add easily 
    any new chat completion  

    Usage:
        factory = ChatCompletionFactory()
        chat_completion = factory.create_chat_completion("gpt")

    Attributes:
        None

    Methods:
        create_chat_completion(completion_type):
            Create a chat completion instance based on the specified type.

    Raises:
        ValueError: If an invalid completion_type is provided.
    """
    @staticmethod
    def create_chat_completion(completion_type) -> ChatCompletionBase:
        """
        Create a chat completion instance based on the specified type.

        Args:
            completion_type (str): The type of completion system to create.

        Returns:
            ChatCompletionBase: An instance of the chat completion system.

        Raises:
            ValueError: If an invalid completion_type is provided.
        """
        if completion_type == "gpt":
            return GPTChatCompletion()
        # Add more completion system types as needed
        else:
            raise ValueError(ERROR_INVALID_COMPLETION_TYPE)