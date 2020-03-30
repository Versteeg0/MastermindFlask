import sqlite3 as db


class Database:
    def __init__(self):
        self.connection = db.connect('mastermind.db')
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                            ([id] INTEGER PRIMARY KEY,[username] VARCHAR, 
                            [date] date, [times_guessed] integer)''')
        self.connection.commit()

    def save_user(self, username, date, times_guessed):
        self.cursor.execute("INSERT INTO leaderboard(username, times_played, times_guessed) VALUES (?, ?, ?)",
                            (username, date, times_guessed,))
        self.connection.commit()

    def get_username(self, username):
        self.cursor.execute("SELECT username FROM leaderboard WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.connection.close()
