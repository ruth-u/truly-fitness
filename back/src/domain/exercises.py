import sqlite3


class Exercise:
    def __init__(self, id, name, description, img, category):
        self.id = id
        self.name = name
        self.description = description
        self.img = img
        self.category = category

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "img": self.img,
            "category": self.category,
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
                id INTEGER PRIMARY KEY,
                name VARCHAR,
                description VARCHAR,
                img TEXT,
                category TEXT
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

    def get_exercise_by_id(self, id):
        sql = """SELECT * FROM exercises WHERE id = :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})
        data = cursor.fetchone()
        exercise = Exercise(**data)
        return exercise

    def get_advanced_exercises(self):
        sql = """SELECT * FROM exercises where id>=21"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        result = []
        for i in data:
            exercise = Exercise(**i)
            result.append(exercise)
        return result

    def get_basic_exercises(self):
        sql = """SELECT * FROM exercises where id<21"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        result = []
        for i in data:
            exercise = Exercise(**i)
            result.append(exercise)
        return result

    def save(self, exercise):
        sql = """insert into exercises (id, name, description, img, category) 
                    values (:id, :name, :description, :img, :category)"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, exercise.to_dict())

        conn.commit()
