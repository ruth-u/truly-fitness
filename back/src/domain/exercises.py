import sqlite3


class Exercise:
    def __init__(self, id, user_id, name, description):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
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
        sql = """CREATE TABLE if not exist exercises (
                id VARCHAR PRIMAREY KEY,
                user_id VRCHAR,
                name VRCHAR,
                description VARVHAR,
                FOREING KEY (user_id) references users (id)
                
        )"""
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


def save(self, exercises):
    sql = """insert into exercises (id, user_id, description) 
                 values (:id, :user_id, :weight, :description)"""
    conn = self.create_conn()
    cursor = conn.cursor()
    exercise = exercises.to_dict()
    cursor.execute(
        sql,
        {
            "id": exercise["id"],
            "user_id": exercise["user_id"],
            "name": exercise["name"],
            "description": exercise["description"],
        },
    )

    conn.commit()
