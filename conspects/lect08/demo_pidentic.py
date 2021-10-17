# виртуальное окружение нужно чтобы изолировать друг от друга зависимости и работать над разными проектами на одной машине
# venv - это слепок того, что надо чтобы работало приложение
# делятся файлами requirements.txt, а не venv, потому что иначе всё ломается
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime = Field(default_factory=datetime.now)
    status: str = 'active'

def get_user(user_id: int) -> User:
    return User(id=user_id, username="john", email='john@example.com')

def main():
    user = get_user(42)
    print(user)

if __name__ == '__main__':
    main()
    