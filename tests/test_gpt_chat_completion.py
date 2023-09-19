import pytest
from unittest.mock import Mock, patch
from app.models.chat_completion import GPTChatCompletion

class TestGPTChatCompletion:
    
    @pytest.fixture
    def gpt_chat_completion(self):
        return GPTChatCompletion()

    @patch('app.models.chat_completion.openai.ChatCompletion.create')
    def test_generate_completion_successful(self,mock_create, gpt_chat_completion):
        mock_response = Mock()
        mock_response.configure_mock(choices=[Mock(message="Chatbot response")])

        mock_create.return_value = mock_response

        messages_history = ["mock message history"]
        completion_message = gpt_chat_completion.generate_completion(messages_history)

        assert completion_message == "Chatbot response"

    @patch('app.models.chat_completion.openai.ChatCompletion.create')
    def test_generate_completion_error(self,mock_create, gpt_chat_completion):
        mock_create.side_effect = Exception("OpenAI API error")

        messages_history = ["mock message history"]

        with pytest.raises(Exception) as e:
            gpt_chat_completion.generate_completion(messages_history)
        
        assert str(e.value) == "OpenAI API error"
