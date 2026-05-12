from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient


class CreateUserRequest(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами эндпоинта /api/v1/users.
    """

    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Создаёт пользователя через POST-запрос к эндпоинту /api/v1/users.

        :param request: Словарь с данными для создания пользователя.
        :return: Объект httpx.Response с ответом сервера.
        """
        return self.post("/api/v1/users", json=request)