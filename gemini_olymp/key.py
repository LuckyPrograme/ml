from pathlib import Path

# ХРАНИТСЯ В РЕПОЗИТОРИИ
KEY_PREFIX = ""

KEY_FILE = Path.home() / ".gemini_last5"


def get_api_key():
    if KEY_FILE.exists():
        last4 = KEY_FILE.read_text().strip()
    else:
        last4 = input("Enter last 4 symbols of Gemini API key: ").strip()
        if len(last4) != 4:
            raise ValueError("Need exactly 4 symbols")
        KEY_FILE.write_text(last4)

    return KEY_PREFIX + last4
