from typing import Any
import reflex as rx
import school_bus_app.utils as utils
from school_bus_app.styles.styles import Size
from school_bus_app.styles.colors import Color
from school_bus_app.components.navbar import navbar
from school_bus_app.routes import Route
from school_bus_app.components.navbar import navbar
from school_bus_app.states.parents_state import ParentsState




def table_kids() -> rx.Component:
    return rx.table_container(
        rx.table(
            headers=["Nombre", "Apellido", "Edad", "Colegio"],
            rows=[
                ("John", 30, "New York"),
                ("Jane", 31, "San Francisco"),
                ("Joe", 32, "Los Angeles"),
            ],
            variant="unstyled",
        )
    )
            