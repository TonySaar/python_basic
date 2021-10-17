from dataclasses import dataclass
from datetime import date



# применяется когда из функции должен вернуться объект с определенными свойствами, грубо оговря как подсказка, что ждем


@dataclass
class User:
    id: int
    username: str
    email: str
    birth_date: date

def get_user(user_id: int):
    username = 'john'
    email = "johnsmith@example.com"
    birth_date = date(1989, 9, 24)
    user = User(id=user_id, username=username, email=email, birth_date=birth_date)


# виртуальное окружение нужно чтобы изолировать друг от друга зависимости и работать над разными проектами на одной машине
# venv - это слепок того, что надо чтобы работало приложение
# делятся файлами requirements.txt, а не venv, потому что иначе всё ломается