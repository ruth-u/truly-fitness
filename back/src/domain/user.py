import sqlite3


class User:
    def __init__(self, id, full_name, user_name, password):
        self.id = id
        self.full_name = full_name
        self.user_name = user_name
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "user_name": self.user_name,
            "password": self.password,
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
               full_name VARCHAR,
               user_name VARCHAR,
               password VARCHAR
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

    def get_by_user_name(self, user_name):
        sql = """SELECT * FROM users WHERE user_name=:user_name"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"user_name": user_name})

        data = cursor.fetchone()
        if data is None:
            return None
        else:
            user = User(**data)
        return user

    def save(self, user):
        sql = """insert or replace into users (id, full_name, user_name, password) 
                 values (:id, :full_name, :user_name, :password)"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "id": user.id,
                "full_name": user.full_name,
                "name": user.user_name,
                "password": user.password,
            },
        )

        conn.commit()
