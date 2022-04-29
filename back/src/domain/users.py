import sqlite3


class User:
    def __init__(self, id, user_name, weight, height, experiencie):
        self.id = id
        self.user_name = user_name
        self.weight = weight
        self.height = height
        self.experiencie = experiencie

    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "weight": self.weight,
            "height": self.height,
            "experiencie": self.experiencie,
        }


class UserRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists users (
               id VARCHAR PRIMARY KEY,
               user_name VARCHAR,
               weight VARCHAR,
               height VARCHAR,
               experiencie NUMERIC
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_users(self):
        sql = """select * from users"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        all_users = [User(**item) for item in data]

        return all_users

    def save(self, user):
        sql = """insert or replace into users (id, user_name, weight, height, experiencie) 
                 values (:id, :user_name, :weight, :height, :experiencie)"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            user.to_dict(),
        )

        conn.commit()
