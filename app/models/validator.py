from constants import (ERROR_EMPTY_JSON, ERROR_INVALID_JSON,
                       ERROR_MISSING_MESSAGE, ERROR_UNSPORTED_MEDIA)

from werkzeug.exceptions import BadRequest, UnsupportedMediaType
from flask import jsonify


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
                   and either validated message or a JSON error response.

                   If validation fails, the second element of the tuple will be a JSON
                   error response, and the first element will be False (not valid).

                   If validation succeeds, the second element of the tuple will be the validated message, and the first element will be True (valid).
        """
        try:
            user_message = request.json
        except UnsupportedMediaType:
            # Not JSON request
            return False, (jsonify({"error": ERROR_UNSPORTED_MEDIA}), 415)
        except BadRequest:
            # Handle invalid JSON format
            return False, (jsonify({"error": ERROR_INVALID_JSON}), 400)

        if not user_message:
            return False, (jsonify({"error": ERROR_EMPTY_JSON}), 400)

        message = user_message.get("message")
        if not message:
            return False, (jsonify({"error": ERROR_MISSING_MESSAGE}), 400)

        return True, message
