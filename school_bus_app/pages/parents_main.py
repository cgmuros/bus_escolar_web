import reflex as rx
import school_bus_app.utils as utils
from school_bus_app.components.navbar import navbar
from school_bus_app.routes import Route
from school_bus_app.components.navbar import navbar
from school_bus_app.states.page_state import PageState
from school_bus_app.components.menu_left import menu_left
from school_bus_app.styles.styles import Size



@rx.page(
    route=Route.PARENTS_MAIN.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.meta,
    on_load=PageState.validate_token,
)
def parents_main() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.box(
            rx.hstack(
                rx.chakra.box(
                    menu_left(),
                    width="25%",
                    padding=Size.SMALL.value,
                ),
                rx.chakra.box(
                    rx.chakra.center(
                        rx.chakra.text(f"Bienvenido {PageState.username}"),
                    ),
                    width="75%",
                ),
            ),
            max_width="100%",
        )
    )