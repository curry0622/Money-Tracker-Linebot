import datetime

# from transitions.extensions import GraphMachine
from transitions import Machine

from utils import send_text_message,send_image_message, send_action_menu, send_expense_type_menu, send_check_menu
from database import Database
from plot import plotExpense

class TocMachine(object):
    def __init__(self, **machine_configs):
        self.machine = Machine(model=self, **machine_configs)

    ''' is going to state '''

    def is_going_to_check(self, event):
        text = event["message"]["text"]
        return text == "查詢"

    def is_going_to_dateInfo(self, event):
        text = event["message"]["text"] if "message" in event else event["postback"]["params"]["date"]
        try:
            datetime.datetime.strptime(text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def is_going_to_monthExpense(self, event):
        return event["message"]["text"] == "這個月的支出結構"

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
        return True

    def is_going_to_description(self, event):
        return True

    ''' on enter state '''

    def on_enter_check(self, event):
        self.db = Database(event["source"]["userId"])
        reply_token = event["replyToken"]
        send_check_menu(reply_token)

    def on_enter_dateInfo(self, event):
        dateStr = event["message"]["text"] if "message" in event else event["postback"]["params"]["date"]
        dateInfoStr = self.db.getDateInfo(dateStr)
        reply_token = event["replyToken"]
        send_text_message(reply_token, dateInfoStr)
        self.go_back()

    def on_enter_monthExpense(self, event):
        reply_token = event["replyToken"]
        month = datetime.datetime.now().strftime("%m")
        monthInfo = self.db.getMonthInfo(month)
        expense = self.db.infoParser(monthInfo)

        # draw pie chart
        # plt.rcParams["font.size"] = 44.0
        # plt.rcParams["font.sans-serif"] = "Microsoft Yahei"
        # newValues, newLabels, colors, separate = valuesHandler(expense)
        # plt.figure(figsize=(20,15))
        # plt.axis("equal")
        # plt.pie(newValues, labels = newLabels, colors = colors, explode = separate, autopct = "%1.1f%%")
        # plt.savefig("./img/month-expense.png", dpi = 30)

        # # upload imgur
        # CLIENT_ID = "b57c8df3844ca8d"
        # PATH = "./img/month-expense.png"
        # url = pyimgur.Imgur(CLIENT_ID).upload_image(PATH, title = "month-expense").link

        # send image message
        url = plotExpense(expense, "month-expense.png")
        print(url)
        send_image_message(reply_token, url)
        self.go_back()

    def on_enter_record(self, event):
        # event["message"]["text"] = 記帳
        self.db = Database(event["source"]["userId"])
        # self.db.insert((None, "default", "default", 0, "default", "default"))
        self.db.insert((None, "default", "default", 0, "default", "default", "default", "default", "default", "default"))
        reply_token = event["replyToken"]
        send_action_menu(reply_token)

    def on_enter_action(self, event):
        # event["message"]["text"] = 支出
        self.db.updateOneColInLastRow("action", event["message"]["text"])
        reply_token = event["replyToken"]
        send_expense_type_menu(reply_token)


    def on_enter_type(self, event):
        # event["message"]["text"] = 食
        self.db.updateOneColInLastRow("type", event["message"]["text"])
        reply_token = event["replyToken"]
        send_text_message(reply_token, "請輸入金額")

    def on_enter_value(self, event):
        # event["message"]["text"] = 金額
        self.db.updateOneColInLastRow("value", event["message"]["text"])
        self.db.updateOneColInLastRow("description", "No description")
        reply_token = event["replyToken"]
        send_text_message(reply_token, "再為這筆記錄增添一些註解吧~")

    # def on_enter_description(self, event):
    #     self.db.updateOneColInLastRow("description", event["message"]["text"])
    #     formatedTime = datetime.datetime.fromtimestamp(event["timestamp"] / 1000).strftime("%Y-%m-%d")
    #     self.db.updateOneColInLastRow("time", formatedTime)
    #     reply_token = event["replyToken"]
    #     balance = self.db.getBalance()
    #     send_text_message(reply_token, "目前結餘: " + str(balance))
    #     self.go_back()

    def on_enter_description(self, event):
        # parsing timestamp
        timestamp = datetime.datetime.fromtimestamp(event["timestamp"] / 1000)
        time = timestamp.strftime("%H:%M:%S")
        date = timestamp.strftime("%Y-%m-%d")
        year = timestamp.strftime("%Y")
        month = timestamp.strftime("%m")
        week = timestamp.strftime("%U")

        # update
        self.db.updateOneColInLastRow("description", event["message"]["text"])
        self.db.updateOneColInLastRow("time", time)
        self.db.updateOneColInLastRow("date", date)
        self.db.updateOneColInLastRow("year", year)
        self.db.updateOneColInLastRow("month", month)
        self.db.updateOneColInLastRow("week", week)
        reply_token = event["replyToken"]
        balance = self.db.getBalance()
        send_text_message(reply_token, "目前結餘: " + str(balance))
        self.go_back()