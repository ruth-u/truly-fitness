import sqlite3


class Exercise:
    def __init__(self, id, name, description, img, week_day, week):
        self.id = id
        self.name = name
        self.description = description
        self.img = img
        self.week_day = week_day
        self.week = week

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "img": self.img,
            "week_day": self.week_day,
            "week": self.week,
        }


class ExerciseRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """CREATE TABLE if not exists exercises (
                id VARCHAR PRIMARY KEY,
                name VARCHAR,
                description VARCHAR,
                img VARCHAR,
                week_day VARCHAR,
                week VARCHAR
                )

        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_exercises(self):
        sql = """select * from exercises"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        result = []
        for item in data:
            exercise = Exercise(**item)
            result.append(exercise)
        return result

    def save(self, exercise):
        sql = """insert into exercises (id, name, description, img, week_day, week) 
                    values (:id, :name, :description, :img, :week_day, :week)"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, exercise.to_dict())

        conn.commit()
