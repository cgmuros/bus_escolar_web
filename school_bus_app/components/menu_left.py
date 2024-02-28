import reflex as rx
from school_bus_app.styles.colors import Color
from school_bus_app.routes import Route
from school_bus_app.states.page_state import PageState
from school_bus_app.components.button_menu import button_menu




def menu_left() -> rx.Component:
    return rx.box(
        rx.chakra.vstack(
            button_menu("Ver rutas", "#"),
            button_menu("Mis Pagos", "#"),
            button_menu("Mis Estudiantes", Route.PARENTS_KIDS.value),

            rx.chakra.button(
                rx.chakra.link(
                    "Cerrar Sesion", 
                    color=Color.CONTENT.value, 
                    on_click=PageState.logout, 
                    style={':hover': {'color': '#808080', 'background-color': 'transparent'}},),
            ),
            # align="flex-start",
            align_items="left",
            # padding=Size.VERY_BIG.value,
            width="100%",
            # align_items="flex-start",
            # align_content="flex-start",
        ),
        width="100%",
        # align_items="flex-start",
        # align_content="flex-start",
    )