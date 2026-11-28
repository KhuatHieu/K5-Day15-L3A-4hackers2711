"""Kiểm bộ nối model bằng python -m unittest discover -s codebase -v."""

import io
import unittest
from urllib.error import HTTPError
from unittest.mock import patch

import ai


class OpenAIAdapterTest(unittest.TestCase):
    def test_call_model_uses_openai_usage_and_messages(self):
        response = {
            "choices": [{"message": {"content": '{"dich_vu":"BaoThuc Pro"}'}}],
            "usage": {
                "prompt_tokens": 35,
                "completion_tokens": 21,
                "completion_tokens_details": {"reasoning_tokens": 8},
            },
        }
        with patch.multiple(ai, MODEL_PROVIDER="openai", MODEL_NAME="gpt-6-luna",
                            OPENAI_API_KEY="test-openai-credential"), patch(
            "ai.post_json", return_value=response
        ) as post:
            result = ai.call_model("Chỉ trả JSON", "GOOGLE *BaoThuc Pro")
        self.assertEqual(result, {
            "text": '{"dich_vu":"BaoThuc Pro"}', "model": "gpt-6-luna",
            "tokens_in": 35, "tokens_out": 21,
        })
        post.assert_called_once_with(ai.URL_OPENAI, {"Authorization": "Bearer test-openai-credential"}, {
            "model": "gpt-6-luna", "store": False,
            "messages": [
                {"role": "developer", "content": "Chỉ trả JSON"},
                {"role": "user", "content": "GOOGLE *BaoThuc Pro"},
            ],
        })

    def test_missing_openai_key_does_not_send_other_providers_key(self):
        with patch.multiple(ai, MODEL_PROVIDER="openai", MODEL_NAME="gpt-6-luna",
                            OPENAI_API_KEY="", API_KEY="test-other-provider-key"), patch("ai.post_json") as post:
            with self.assertRaisesRegex(ValueError, "OPENAI_API_KEY"):
                ai.call_model("", "kiểm")
            post.assert_not_called()

    def test_http_errors_redact_the_request_credential(self):
        request_error = HTTPError(
            ai.URL_OPENAI, 401, "Unauthorized", {}, io.BytesIO(b"Invalid test-openai-credential"),
        )
        with patch("ai.urllib.request.urlopen", side_effect=request_error):
            with self.assertRaisesRegex(RuntimeError, r"HTTP 401: Invalid \[ẩn\]"):
                ai.post_json(ai.URL_OPENAI, {"Authorization": "Bearer test-openai-credential"}, {})
