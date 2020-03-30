import datetime
import sqlite3 as db


class Database:
    def __init__(self):
        self.connection = db.connect('mastermind.db')
        self.cursor = self.connection.cursor()

    def test_data(self):
        self.cursor.execute("INSERT INTO leaderboard(username, times_guessed) VALUES (?, ?)",
                            ("ricobender", 5,))
        self.connection.commit()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                            ([id] INTEGER PRIMARY KEY,[username] text, 
                            [date] date, [times_guessed] integer)''')
        self.connection.commit()

    def save_user(self, username, date, times_guessed):
        self.cursor.execute("INSERT INTO leaderboard(username, times_played, times_guessed) VALUES (?, ?, ?)",
                            (username, date, times_guessed,))
        self.connection.commit()

    def get_user(self, username):
        self.cursor.execute("SELECT username FROM leaderboard WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_scores(self, username):
        self.cursor.execute("SELECT username FROM leaderboard WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.connection.close()
