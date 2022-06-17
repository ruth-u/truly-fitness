import sqlite3


class UserExercise:
    def __init__(self, user_id, exercise_id, exercise_date, exercise_done):
        self.user_id = user_id
        self.exercise_id = exercise_id
        self.exercise_date = exercise_date
        self.exercise_done = exercise_done

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "exercise_id": self.exercise_id,
            "exercise_date": self.exercise_date,
            "exercise_done": self.exercise_done,
        }


class UserExerciseRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """create table if not exists users_exercises (
                user_id varchar,
                exercise_id varchar,
                exercise_date varchar,
                exercise_done varchar,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (exercise_id) REFERENCES exercises (id),
                FOREIGN KEY (exercise_date) REFERENCES users (register_date)
                )

        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_exercises(self):
        sql = """select * from users_exercises"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        result = []
        for item in data:
            exercise = UserExercise(**item)
            result.append(exercise)
        return result

    def save_user_exercises(self, user_exercise):
        sql = """insert into users_exercises (user_id, exercise_id, exercise_date, exercise_done)
                    values (:user_id, :exercise_id, :exercise_date, :exercise_done)"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, user_exercise.to_dict())

        conn.commit()
