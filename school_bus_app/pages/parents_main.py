import reflex as rx
import school_bus_app.utils as utils
from school_bus_app.components.navbar import navbar
from school_bus_app.routes import Route
from school_bus_app.components.navbar import navbar
from school_bus_app.states.parents_state import ParentsState
from school_bus_app.components.menu_left import menu_left



@rx.page(
    route=Route.PARENTS_MAIN.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.meta,
    on_load=ParentsState.get_username_from_token,
)
def parents_main() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.hstack(
                menu_left(),
                rx.box(
                    rx.center(
                        rx.text(f"Bienvenido {ParentsState.username}"),
                    ),
                    width="75%",
                ),
            ),
            max_width="100%",
        ),
    )