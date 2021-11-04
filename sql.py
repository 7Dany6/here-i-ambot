import sqlite3


class SQL:
    def __init__(self, database_file):
        """
        Connecting to the database
        """
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, contact):
        """
        Searching a given person in the database
        """
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `contact` = ?", (contact,)).fetchall()
        return bool(len(result))

    def register(self, username, name, id, contact):
        """
        Registration of a user
        """
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` VALUES (?, ?, ?, ?)", (username, name, id, contact))

    def tracked_id(self, contact):
        """
        Find id of a tracked person
        """
        with self.connection:
            return self.cursor.execute("SELECT id FROM `users` WHERE `contact` = ?", (contact,)).fetchall()

    def get_name(self, id):
        """
        Finds name of a person by his id
        """
        with self.connection:
            return self.cursor.execute("SELECT name FROM `users` WHERE `id` = ?", (id,)).fetchall()

    def get_contact(self, id):
        """
        Finds contact of a person by his id
        """
        with self.connection:
            return self.cursor.execute("SELECT contact FROM `users` WHERE `id` = ?", (id,)).fetchall()

    def get_username(self, id):
        """
        Finds username of a person
        """
        with self.connection:
            return self.cursor.execute("SELECT username FROM `users` WHERE `id` = ?", (id,)).fetchall()

    def delete_account(self, id):
        """
        Deletes a user from a database
        """
        with self.connection:
            return self.cursor.execute("DELETE FROM `users` WHERE `id` = ?", (id,)).fetchall()