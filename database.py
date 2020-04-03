import datetime
import sqlite3 as db


class Database:
    def __init__(self):
        self.connection = db.connect('mastermind.db')
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                            ([id] INTEGER PRIMARY KEY,[username] text, 
                            [date] date, [times_guessed] integer, [godmode] integer)''')
        self.connection.commit()

    def save_user(self, username, date, times_guessed, godmode):
        self.cursor.execute("INSERT INTO leaderboard(username, date, times_guessed, godmode) VALUES (?, ?, ?, ?)",
                            (username, date, times_guessed, godmode,))
        self.connection.commit()

    def get_user(self, username):
        self.cursor.execute("SELECT username FROM leaderboard WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_scores(self, username):
        self.cursor.execute("SELECT date, times_guessed, godmode FROM leaderboard WHERE username = ?", (username,))
        return self.cursor.fetchall()