import sqlite3

class Database:
	def __init__(self, userId):
        self.userId = userId
        self.con = sqlite3.connect(userId + ".db")
        self.cur = self.con.cursor()

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
        self.cur.executemany(insertStr, data)
        self.con.commit()

    def returnAll(self):
        return self.cur.execute("SELECT * FROM " + self.userId + " ORDER BY id")