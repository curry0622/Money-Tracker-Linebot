import os
import sys
import json

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_main_menu

load_dotenv()

machine = TocMachine(
    states=["user", "check", "record", "action", "type", "value", "description"],
    transitions=[
		{
            "trigger": "advance",
            "source": "user",
            "dest": "check",
            "conditions": "is_going_to_check",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "record",
            "conditions": "is_going_to_record",
        },
		{
            "trigger": "advance",
            "source": "record",
            "dest": "action",
            "conditions": "is_going_to_action",
        },
		{
            "trigger": "advance",
            "source": "action",
            "dest": "type",
            "conditions": "is_going_to_type",
        },
		{
            "trigger": "advance",
            "source": "type",
            "dest": "value",
            "conditions": "is_going_to_value",
        },
        {
            "trigger": "advance",
            "source": "value",
            "dest": "description",
            "conditions": "is_going_to_description",
        },
        {"trigger": "go_back", "source": ["check", "description"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)



def webhook_parser(webhook):
    event = webhook["events"][0]
    reply_token = event["replyToken"]
    user_id = event["source"]["userId"]
    message = event["message"]["text"]
    return event, reply_token, user_id, message



@app.route("/webhook", methods=["POST"])
def webhook_handler():
    webhook = json.loads(request.data.decode("utf-8"))
    if(len(webhook["events"]) > 0):
        event, reply_token, user_id, message = webhook_parser(webhook)
        response = machine.advance(event)
        # check if message is valid or not
        if response == False:
            if machine.state == 'user':
                send_main_menu(reply_token)
            elif machine.state == 'record':
                send_text_message(reply_token, "請輸入支出或收入")
            elif machine.state == 'action':
                send_text_message(reply_token, "請輸入種類\n食、衣、住、行、育、樂")
            elif machine.state == 'type':
                send_text_message(reply_token, "請輸入金額")


    return "OK"


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
