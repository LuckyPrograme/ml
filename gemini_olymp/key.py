from pathlib import Path

# ХРАНИТСЯ В РЕПОЗИТОРИИ
KEY_PREFIX = "AIzaSyDXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # всё, кроме 5 последних

KEY_FILE = Path.home() / ".gemini_last5"


def get_api_key():
    if KEY_FILE.exists():
        last5 = KEY_FILE.read_text().strip()
    else:
        last5 = input("Enter last 5 symbols of Gemini API key: ").strip()
        if len(last5) != 5:
            raise ValueError("Need exactly 5 symbols")
        KEY_FILE.write_text(last5)

    return KEY_PREFIX + last5
