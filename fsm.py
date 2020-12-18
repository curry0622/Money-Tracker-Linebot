# from transitions.extensions import GraphMachine
from transitions import Machine

from utils import send_text_message


class TocMachine(object):
    def __init__(self, **machine_configs):
        self.machine = Machine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        # text = event.message.text
        text = event["message"]["text"]
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        # text = event.message.text
        text = event["message"]["text"]
        return text.lower() == "go to state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        # reply_token = event.reply_token
        reply_token = event["replyToken"]
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        # reply_token = event.reply_token
        reply_token = event["replyToken"]
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
