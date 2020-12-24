import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, ImageSendMessage


from messageTemplate import mainMenu, actionMenu, expenseTypeMenu, checkMenu, imgMsg

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def sendImg(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url=url, preview_image_url=url))

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"

def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage("主選單", imgMsg(url)))
    return "OK"

def send_main_menu(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage("主選單", mainMenu))
    return "OK"

def send_action_menu(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage("收支選單", actionMenu))
    return "OK"

def send_expense_type_menu(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage("支出種類選單", expenseTypeMenu))
    return "OK"

def send_check_menu(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage("查詢選單", checkMenu()))
    return "OK"
