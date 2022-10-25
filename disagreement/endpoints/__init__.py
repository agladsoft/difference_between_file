from .home import router as home_page
from .uploaddocs import router as uploaddocs


list_of_routes = [home_page, uploaddocs]


__all__ = [
    "list_of_routes",
]
