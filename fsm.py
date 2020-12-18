# from transitions.extensions import GraphMachine
from transitions import Machine

from utils import send_text_message


class TocMachine(object):
    def __init__(self, **machine_configs):
        self.machine = Machine(model=self, **machine_configs)

    def is_going_to_check(self, event):
        text = event["message"]["text"]
        return text == "查詢"

    def is_going_to_record(self, event):
        text = event["message"]["text"]
        return text == "記帳"

    def is_going_to_action(self, event):
        text = event["message"]["text"]
        return text == "收入" or text == "支出"

    def is_going_to_type(self, event):
        text = event["message"]["text"]
        return text == "食" or text == "衣" or text == "住" or text == "行" or text == "育" or text == "樂"

    def is_going_to_value(self, event):
        text = event["message"]["text"]
        return True

    def on_enter_check(self, event):
        print("I'm entering check")

        # reply_token = event.reply_token
        reply_token = event["replyToken"]
        send_text_message(reply_token, "查詢失敗")
        self.go_back()

    def on_enter_record(self, event):
        print("I'm entering record")

        # reply_token = event.reply_token
        reply_token = event["replyToken"]
        send_text_message(reply_token, "請輸入支出或收入")

    def on_enter_action(self, event):
        print("I'm entering action")

        # reply_token = event.reply_token
        reply_token = event["replyToken"]
        send_text_message(reply_token, "請輸入種類\n食、衣、住、行、育、樂")

    def on_enter_type(self, event):
        print("I'm entering type")

        # reply_token = event.reply_token
        reply_token = event["replyToken"]
        send_text_message(reply_token, "請輸入金額")

    def on_enter_value(self, event):
        print("I'm entering value")

        # reply_token = event.reply_token
        reply_token = event["replyToken"]
        send_text_message(reply_token, "已紀錄")
        self.go_back()

# class TocMachine(object):
#     def __init__(self, **machine_configs):
#         self.machine = Machine(model=self, **machine_configs)

#     def is_going_to_state1(self, event):
#         # text = event.message.text
#         text = event["message"]["text"]
#         return text.lower() == "go to state1"

#     def is_going_to_state2(self, event):
#         # text = event.message.text
#         text = event["message"]["text"]
#         return text.lower() == "go to state2"

#     def is_going_to_state3(self, event):
#         # text = event.message.text
#         text = event["message"]["text"]
#         return text.lower() == "go to state3"

#     def on_enter_state1(self, event):
#         print("I'm entering state1")

#         # reply_token = event.reply_token
#         reply_token = event["replyToken"]
#         send_text_message(reply_token, "Trigger state1")
#         self.go_back()

#     def on_exit_state1(self):
#         print("Leaving state1")

#     def on_enter_state2(self, event):
#         print("I'm entering state2")

#         # reply_token = event.reply_token
#         reply_token = event["replyToken"]
#         send_text_message(reply_token, "Trigger state2")
#         self.go_back()

#     def on_exit_state2(self):
#         print("Leaving state2")

#     def on_enter_state3(self, event):
#         print("I'm entering state3")

#         # reply_token = event.reply_token
#         reply_token = event["replyToken"]
#         send_text_message(reply_token, "Trigger state3")
#         self.go_back()

#     def on_exit_state3(self):
#         print("Leaving state3")