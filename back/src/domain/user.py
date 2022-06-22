import sqlite3


class User:
    def __init__(
        self,
        id,
        user_name,
        password,
        first_name,
        last_name,
        goal,
        weight,
        height,
        experiencie,
        register_date,
    ):
        self.id = id
        self.user_name = user_name
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.goal = goal
        self.weight = weight
        self.height = height
        self.experiencie = experiencie
        self.register_date = register_date

    def full_name(self):
        return self.first_name + " " + self.last_name

    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name(),
            "goal": self.goal,
            "weight": self.weight,
            "height": self.height,
            "experiencie": self.experiencie,
            "register_date": self.register_date,
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
               password VARCHAR,
               first_name VARCHAR,
               last_name VARCHAR, 
               goal VARCHAR, 
               weight VARCHAR, 
               height VARCHAR, 
               experiencie INTEGER,
               register_date VARCHAR
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
            user = User(
                id=data["id"],
                user_name=data["user_name"],
                password=data["password"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                goal=data["goal"],
                weight=data["weight"],
                height=data["height"],
                experiencie=data["experiencie"],
                register_date=data["register_date"],
            )
        return user

    def get_user_by_experiencie(self, experiencie):
        sql = """SELECT * FROM users WHERE experiencie=:experiencie"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"experiencie": experiencie})

        data = cursor.fetchall()
        result = []
        for item in data:
            user = User(
                id=item["id"],
                user_name=item["user_name"],
                password=item["password"],
                first_name=item["first_name"],
                last_name=item["last_name"],
                goal=item["goal"],
                weight=item["weight"],
                height=item["height"],
                experiencie=item["experiencie"],
                register_date=item["register_date"],
            )
            result.append(result)
        return result

    def save(self, user):
        sql = """insert or replace into users (id, user_name, password, first_name, last_name, goal, weight, height, experiencie, register_date) 
                 values (:id, :user_name, :password, :first_name, :last_name, :goal, :weight, :height, :experiencie, :register_date)"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, user.to_dict())

        conn.commit()
