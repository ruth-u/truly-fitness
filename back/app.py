from src.webserver import create_app
from src.domain.user import UserRepository
from src.domain.exercises import ExerciseRepository


database_path = "data/database.db"

repositories = {
    "users": UserRepository(database_path),
    "exercises": ExerciseRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
