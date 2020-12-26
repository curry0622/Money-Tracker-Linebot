import sqlite3
import datetime


class Database:
    def __init__(self, userId):
        self.userId = userId
        self.con = sqlite3.connect("./db/" + userId + ".db", check_same_thread=False)
        self.cur = self.con.cursor()
        self.createTable()

    def createTable(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS " + self.userId + " ( "
            + "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            + "action TEXT NOT NULL, "
            + "type TEXT NOT NULL, "
            + "value INTEGER DEFAULT 0, "
            + "description TEXT, "
            + "time TEXT NOT NULL, "
            + "date TEXT NOT NULL, "
            + "year TEXT NOT NULL, "
            + "month TEXT NOT NULL, "
            + "week TEXT NOT NULL)"
        )

    def insert(self, data):
        insertStr = "INSERT INTO " + self.userId + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.cur.execute(insertStr, data)
        self.con.commit()

    def returnAll(self):
        return self.cur.execute("SELECT * FROM " + self.userId + " ORDER BY id")

    def returnLastId(self):
        return self.cur.execute("SELECT * FROM " + self.userId + " ORDER BY id DESC LIMIT 1").fetchone()[0]

    def returnLastRow(self):
        return self.cur.execute("SELECT * FROM " + self.userId + " ORDER BY id DESC LIMIT 1").fetchone()

    def updateOneColInLastRow(self, col, data):
        lastId = self.returnLastId()
        updateStr = "UPDATE " + self.userId + " SET " + col + " = ? WHERE id = ?"
        self.cur.execute(updateStr, (data, lastId))
        self.con.commit()

    def getBalance(self):
        balance = 0
        all = self.returnAll()
        for row in all:
            if type(row[3]) is int:
                if row[1] == "收入":
                    balance += row[3]
                elif row[1] == "支出":
                    balance -= row[3]
        return balance

    def getDateInfo(self, dateStr):
        getStr = "SELECT * FROM " + self.userId + " WHERE date = ?"
        dateInfo = self.cur.execute(getStr, (dateStr, )).fetchall()
        dateInfoStr = "[ " + dateStr + " ]\n"
        index = 1
        expense = 0
        income = 0
        for info in dateInfo:
            if type(info[3]) is int:
                dateInfoStr += "---------------\n"
                dateInfoStr += "編號: " + str(index) + "\n"
                dateInfoStr += "收支: " + info[1] + "\n"
                dateInfoStr += "種類: " + info[2] + "\n"
                dateInfoStr += "金額: " + str(info[3]) + "\n"
                dateInfoStr += "註解: " + info[4] + "\n"
                dateInfoStr += "時間: " + info[5] + "\n"
                index += 1
                if(info[1] == "支出"):
                    expense += info[3]
                elif(info[1] == "收入"):
                    income += info[3]
        dateInfoStr += "---------------\n"
        dateInfoStr += "總支出: " + str(expense) + "\n"
        dateInfoStr += "總收入: " + str(income)
        return dateInfoStr

    def getWeekInfo(self, weekStr):
        week = datetime.datetime.now().strftime("%U")
        getStr = "SELECT * FROM " + self.userId + " WHERE week = ?"
        weekInfo = self.cur.execute(getStr, (weekStr, ))
        return weekInfo

    def getMonthInfo(self, monthStr):
        month = datetime.datetime.now().strftime("%m")
        getStr = "SELECT * FROM " + self.userId + " WHERE month = ?"
        monthInfo = self.cur.execute(getStr, (monthStr, ))
        return monthInfo

    def infoParser(self, info):
        # ["食", "衣", "住", "行", "育", "樂"]
        expense = [0, 0, 0, 0, 0, 0]
        # ["薪資", "獎金", "投資", "零用錢"]
        income = [0, 0, 0, 0]
        for row in info:
            value = row[3]
            if row[2] == "食":
                expense[0] += value
            elif row[2] == "衣":
                expense[1] += value
            elif row[2] == "住":
                expense[2] += value
            elif row[2] == "行":
                expense[3] += value
            elif row[2] == "育":
                expense[4] += value
            elif row[2] == "樂":
                expense[5] += value
            elif row[2] == "薪資":
                income[0] += value
            elif row[2] == "獎金":
                income[1] += value
            elif row[2] == "投資":
                income[2] += value
            elif row[2] == "零用錢":
                income[3] += value
        return expense, income


if __name__ == "__main__":
    db = Database("Ufdbef95a2f854faea6f5a4b458e98747")
    thisWeek = datetime.datetime.now().strftime("%U")
    weekInfo = db.getWeekInfo(thisWeek)
    expense = db.infoParser(weekInfo)
    print(expense)