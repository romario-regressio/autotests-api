from typing import TypedDict

from httpx import Client, Response

from clients.private_http_builder import get_private_http_client


class Exercise(TypedDict):
    """Структура задания."""

    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """Структура query-параметров для получения списка заданий."""

    courseId: str


class GetExercisesResponseDict(TypedDict):
    """Структура ответа получения списка заданий."""

    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    """Структура ответа получения задания."""

    exercise: Exercise


class CreateExerciseRequestDict(TypedDict):
    """Структура запроса создания задания."""

    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """Структура ответа создания задания."""

    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict):
    """Структура запроса обновления задания."""

    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseResponseDict(TypedDict):
    """Структура ответа обновления задания."""

    exercise: Exercise


class ExercisesClient:
    """Клиент для работы с заданиями."""

    def __init__(self, client: Client):
        """Инициализирует клиент заданий.

        Args:
            client: HTTP-клиент.
        """
        self.client = client

    def get_exercise_api(self, exercise_id: str) -> Response:
        """Выполняет API-запрос на получение задания.

        Args:
            exercise_id: Идентификатор задания.

        Returns:
            Ответ от сервера.
        """
        return self.client.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """Выполняет API-запрос на получение списка заданий.

        Args:
            query: Query-параметры запроса.

        Returns:
            Ответ от сервера.
        """
        return self.client.get("/api/v1/exercises", params=query)

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """Выполняет API-запрос на создание задания.

        Args:
            request: Данные для создания задания.

        Returns:
            Ответ от сервера.
        """
        return self.client.post("/api/v1/exercises", json=request)

    def update_exercise_api(
        self,
        exercise_id: str,
        request: UpdateExerciseRequestDict,
    ) -> Response:
        """Выполняет API-запрос на обновление задания.

        Args:
            exercise_id: Идентификатор задания.
            request: Данные для обновления задания.

        Returns:
            Ответ от сервера.
        """
        return self.client.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """Получает задание.

        Args:
            exercise_id: Идентификатор задания.

        Returns:
            JSON-ответ с заданием.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """Получает список заданий.

        Args:
            query: Query-параметры запроса.

        Returns:
            JSON-ответ со списком заданий.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(
        self,
        request: CreateExerciseRequestDict,
    ) -> CreateExerciseResponseDict:
        """Создаёт задание.

        Args:
            request: Данные для создания задания.

        Returns:
            JSON-ответ с созданным заданием.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(
        self,
        exercise_id: str,
        request: UpdateExerciseRequestDict,
    ) -> UpdateExerciseResponseDict:
        """Обновляет задание.

        Args:
            exercise_id: Идентификатор задания.
            request: Данные для обновления задания.

        Returns:
            JSON-ответ с обновлённым заданием.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: dict) -> ExercisesClient:
    """Создаёт клиент для работы с заданиями.

    Args:
        user: Данные пользователя для авторизации.

    Returns:
        Клиент для работы с заданиями.
    """
    return ExercisesClient(client=get_private_http_client(user))