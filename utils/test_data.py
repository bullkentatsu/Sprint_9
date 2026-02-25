from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class UserData:
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


DEFAULT_PASSWORD = "Switch@123"


def generate_user() -> UserData:
    uid = uuid4().hex[:10]
    return UserData(
        first_name=f"Test{uid}",
        last_name=f"User{uid}",
        username=f"autouser_{uid}",
        email=f"autotest_{uid}@example.com",
        password=DEFAULT_PASSWORD,
    )


@dataclass(frozen=True)
class RecipeData:
    title: str
    cooking_time: str
    ingredient: str
    amount: str
    image_filename: str


DEFAULT_RECIPE = RecipeData(
    title="Автотестовый рецепт",
    cooking_time="10",
    ingredient="та",
    amount="1",
    image_filename="sample.jpg",
)