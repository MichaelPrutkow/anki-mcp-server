import json
import urllib.error
import urllib.request
from typing import Any

ANKI_URL = "http://127.0.0.1:8765"
API_VERSION = 6


def request(action: str, **params: Any) -> dict[str, Any]:
    return {"action": action, "params": params, "version": API_VERSION}


def invoke(action: str, **params: Any):
    request_json = json.dumps(request(action, **params)).encode("utf-8")
    try:
        response = json.load(
            urllib.request.urlopen(
                urllib.request.Request(ANKI_URL, request_json), timeout=10
            )
        )
    except urllib.error.URLError as exc:
        raise Exception(
            f"AnkiConnect does not answer at {ANKI_URL}"
            "Is Anki running currently, and is there no Dialoguewindow open?"
        ) from exc
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response["result"]
