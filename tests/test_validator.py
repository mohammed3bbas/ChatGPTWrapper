from app.constants import (ERROR_EMPTY_JSON, ERROR_INVALID_JSON,
                           ERROR_MISSING_MESSAGE, ERROR_UNSPORTED_MEDIA)
from app.models.validator import Validator
from flask import Request


class TestValidator:

    def test_valid_json(self):
        request = Request.from_values(data='{"message": "Hello, world!"}', content_type="application/json")
        
        is_valid, user_message = Validator.chat_request_validator(request)
        
        assert is_valid is True
        assert user_message == "Hello, world!"

    def test_invalid_json(self):
        request = Request.from_values(data="This is not valid JSON", content_type="application/json")
        
        is_valid, error_response = Validator.chat_request_validator(request)
        
        assert is_valid is False
        assert error_response == ({"error": ERROR_INVALID_JSON}, 400)

    def test_empty_json(self):
        request = Request.from_values(data='{}', content_type="application/json")
        
        is_valid, error_response = Validator.chat_request_validator(request)
        
        assert is_valid is False
        assert error_response == ({"error": ERROR_EMPTY_JSON}, 400)

    def test_missing_message(self):
        request = Request.from_values(data='{"not_message": "Hello, world!"}', content_type="application/json")
        
        is_valid, error_response = Validator.chat_request_validator(request)
        
        assert is_valid is False
        assert error_response == ({"error": ERROR_MISSING_MESSAGE}, 400)

    def test_unsupported_media_type(self):
        request = Request.from_values(data='{"message": "Hello, world!"}', content_type="notJson")
        
        is_valid, error_response = Validator.chat_request_validator(request)
        
        assert is_valid is False
        assert error_response == ({"error": ERROR_UNSPORTED_MEDIA}, 415)
