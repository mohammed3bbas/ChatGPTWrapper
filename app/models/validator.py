from app.constants import (ERROR_EMPTY_JSON, ERROR_INVALID_JSON,
                       ERROR_MISSING_MESSAGE, ERROR_UNSPORTED_MEDIA)

from werkzeug.exceptions import BadRequest, UnsupportedMediaType


class Validator:
    """
    Utility class for validation.

    This class provides methods for validating chat request data.
    It can check for JSON format, required fields, and data types.
    """
    @staticmethod
    def chat_request_validator(request):
        """
        Validate a chat request received via Flask's request object.

        Args:
            request (Request): The Flask request object containing the chat request data.

        Returns:
            tuple: A tuple containing a Boolean indicating validation success,
                   and either validated message or a error response.

                   If validation fails, the first element will be False (not valid). the second element will be a tuple, 
                   first element (of the second tuple) will be error response (dictionary), and secod element is response status coded.

                   If validation succeeds, the first element will be True (valid). and the second element of the tuple will be the validated message.
        """
        try:
            user_message = request.json
        except UnsupportedMediaType:
            # Not JSON request
            return False, ({"error": ERROR_UNSPORTED_MEDIA}, 415)
        except BadRequest:
            # Handle invalid JSON format
            return False, ({"error": ERROR_INVALID_JSON}, 400)

        if not user_message:
            return False, ({"error": ERROR_EMPTY_JSON}, 400)

        message = user_message.get("message")
        if not message:
            return False, ({"error": ERROR_MISSING_MESSAGE}, 400)

        return True, message
