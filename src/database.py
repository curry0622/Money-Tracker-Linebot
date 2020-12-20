import sqlite3


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
            + "time TEXT NOT NULL)"
        )

    def insert(self, data):
        insertStr = "INSERT INTO " + self.userId + " VALUES (?, ?, ?, ?, ?, ?)"
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


if __name__ == "__main__":
    testDb = Database("testId")
    testDb.insert((
        None,
        "收入",
        "薪資",
        120000,
        "爽啦",
        "2020/12/20 02:30"
    ))
    print("All in db:")
    for row in testDb.returnAll():
        print(row[0])
    print("Last id in db")
    print(testDb.returnLastId())
    testDb.updateOneColInLastRow("type", "獎學金")
    testDb.updateOneColInLastRow("value", 8000)
    testDb.updateOneColInLastRow("time", "2020/05/20 05:20")
    testDb.updateOneColInLastRow("description", "第一名")
    print(testDb.returnLastRow())