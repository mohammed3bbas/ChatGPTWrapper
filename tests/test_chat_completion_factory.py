import pytest
from app.models.chat_completion import ChatCompletionBase
from app.models.chat_completion_factory import ChatCompletionFactory
from app.constants import ERROR_INVALID_COMPLETION_TYPE, CHAT_MODEL

class TestChatCompletionFactory:

    def test_create_chat_completion_valid_type(self):
        factory = ChatCompletionFactory()

        chat_completion = factory.create_chat_completion(CHAT_MODEL)

        assert isinstance(chat_completion, ChatCompletionBase)

    def test_create_chat_completion_invalid_type(slef):
        factory = ChatCompletionFactory()

        with pytest.raises(ValueError) as e:
            factory.create_chat_completion("invalid_type")

        assert str(e.value) == ERROR_INVALID_COMPLETION_TYPE
