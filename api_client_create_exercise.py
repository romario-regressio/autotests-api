import logging
import time

from clients.authentication.users.public_users_client import get_public_users_client
from clients.courses.courses_client import get_courses_client
from clients.exercises.exercises_client import get_exercises_client
from clients.files.files_client import get_files_client


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    """Создаёт пользователя, файл, курс и задание через API-клиенты."""
    public_users_client = get_public_users_client()

    create_user_data = public_users_client.create_user(
        {
            "email": f"test.{time.time()}@example.com",
            "password": "password",
            "lastName": "string",
            "firstName": "string",
            "middleName": "string",
        }
    )

    logger.info("Create user data: %s", create_user_data)

    user = create_user_data["user"]

    files_client = get_files_client(user)
    courses_client = get_courses_client(user)
    exercises_client = get_exercises_client(user)

    create_file_data = files_client.create_file(
        "courses",
        "image.png",
    )

    logger.info("Create file data: %s", create_file_data)

    file = create_file_data["file"]

    create_course_data = courses_client.create_course(
        {
            "title": "Python",
            "maxScore": 100,
            "minScore": 10,
            "description": "Python API course",
            "previewFileId": file["id"],
            "estimatedTime": "2 weeks",
        }
    )

    logger.info("Create course data: %s", create_course_data)

    course = create_course_data["course"]

    create_exercise_data = exercises_client.create_exercise(
        {
            "title": "Exercise 1",
            "courseId": course["id"],
            "maxScore": 5,
            "minScore": 1,
            "orderIndex": 0,
            "description": "Exercise 1",
            "estimatedTime": "5 minutes",
        }
    )

    logger.info("Create exercise data: %s", create_exercise_data)


if __name__ == "__main__":
    main()