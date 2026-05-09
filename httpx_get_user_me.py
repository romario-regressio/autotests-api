import httpx

login_payload = {
    "email": "bboyonyx225@yandex.ru",
    "password": "261988555"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Status Code; ", login_response.status_code)
print("Login response", login_response_data)

access_token = login_response_data["token"]["accessToken"]
headers = {
    "Authorization": f"Bearer {access_token}"
}
user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
user_response_data = user_response.json()
print("Status Code; ", user_response.status_code)
print("User response", user_response_data)
