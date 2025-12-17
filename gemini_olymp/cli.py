import json
from pathlib import Path
import google.generativeai as genai
from gemini_olymp.key import get_api_key

HISTORY_FILE = Path.home() / ".gemini_history.json"

genai.configure(api_key=get_api_key())
model = genai.GenerativeModel("gemini-1.5-pro")


def load_history():
    if HISTORY_FILE.exists():
        return json.loads(HISTORY_FILE.read_text())
    return []


def save_history(history):
    HISTORY_FILE.write_text(json.dumps(history, ensure_ascii=False, indent=2))


def main():
    history = load_history()
    chat = model.start_chat(history=history)

    if not history:
        chat.send_message(
            "Ты помощник для олимпиад по ИИ. "
            "Отвечай строго: идея → алгоритм → сложность → крайние случаи."
        )

    print("Gemini Olympiad CLI  |  /exit /reset")

    while True:
        q = input(">>> ")
        if q == "/exit":
            save_history(chat.history)
            break
        if q == "/reset":
            chat = model.start_chat(history=[])
            continue

        r = chat.send_message(q)
        print(r.text)


if __name__ == "__main__":
    main()
