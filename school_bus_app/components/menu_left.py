import reflex as rx
import school_bus_app.utils as utils
from school_bus_app.styles.styles import Size
from school_bus_app.styles.colors import Color
from school_bus_app.components.navbar import navbar
from school_bus_app.routes import Route
from school_bus_app.components.navbar import navbar
from school_bus_app.states.parents_state import ParentsState
from school_bus_app.components.button_menu import button_menu




def menu_left() -> rx.Component:
    return rx.chakra.box(
        rx.chakra.vstack(
            button_menu("Ver rutas", "#"),
            button_menu("Mis Pagos", "#"),
            button_menu("Mis Hijos", Route.PARENTS_KIDS.value),

            rx.chakra.button(
                rx.chakra.link(
                    "Cerrar Sesion", 
                    color=Color.CONTENT.value, 
                    on_click=ParentsState.logout, 
                    style={':hover': {'color': '#808080', 'background-color': 'transparent'}},),
            ),
            align_items="left",
            padding=Size.VERY_BIG.value,
        ),
        width="25%",
    )