import reflex as rx
import school_bus_app.utils as utils
from school_bus_app.styles.styles import Size
from school_bus_app.styles.colors import Color
from school_bus_app.components.navbar import navbar
from school_bus_app.routes import Route
from school_bus_app.components.navbar import navbar
from school_bus_app.states.parents_state import ParentsState
from school_bus_app.components.button_menu import button_menu
from school_bus_app.components.table_kids import table_kids
from school_bus_app.components.menu_left import menu_left
from school_bus_app.states.kids_state import KidsState





@rx.page(
    route=Route.PARENTS_KIDS.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.meta,
)
def parents_kids() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.container(
            rx.chakra.hstack(
                menu_left(),
                rx.chakra.box(
                    rx.chakra.box(
                        rx.chakra.text("Agregar Hijo"),
                    ),
                    rx.chakra.center(
                        rx.text(KidsState.clicked_data),
                        table_kids(),
                    ),
                    width="75%",
                ),
            ),
            max_width="100%",
        ),
    )