from flask import Flask, request
import requests
from dotenv import load_dotenv
import os
from os.path import join, dirname
import json

app = Flask(__name__)

def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


def send_message(chat_id, text):
    method = "sendMessage"
    token = get_from_env("TELEGRAM_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


def send_pay_button(chat_id, text):

    method = "sendMessage"
    token = get_from_env("TELEGRAM_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{token}/{method}"

    data = {"chat_id": chat_id, "text": text, "reply_markup": json.dumps({"inline_keyboard": [[{
        "text": "",
        "url": f""
    }]]})}

    requests.post(url, data=data)





@app.route('/', methods=["POST"])
def process():
    chat_id = request.json["object"]["metadata"]["chat_id"]

    return {"ok": True}


if __name__ == '__main__':
    app.run()