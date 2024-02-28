import reflex as rx
import school_bus_app.utils as utils
from school_bus_app.styles.styles import Size
from school_bus_app.components.navbar import navbar
from school_bus_app.routes import Route
from school_bus_app.components.navbar import navbar
from school_bus_app.components.menu_left import menu_left





@rx.page(
    route=Route.PARENTS_KIDS.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.meta,
)
def parents_students() -> rx.Component:
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
                    rx.chakra.box(
                        rx.link(
                            rx.chakra.text("Nuevo"),
                            href=Route.PARENTS_ADD_STUDENT.value,
                        ),
                    ),
                    rx.chakra.box(
                        # table_kids(),
                    ),
                    width="75%",
                ),
            ),
            max_width="100%",
        ),
    )