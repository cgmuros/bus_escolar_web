from typing import Any
import reflex as rx
import school_bus_app.utils as utils
from school_bus_app.styles.styles import Size
from school_bus_app.styles.colors import Color
from school_bus_app.components.navbar import navbar
from school_bus_app.routes import Route
from school_bus_app.components.navbar import navbar
from school_bus_app.states.parents_state import ParentsState




def button_menu(title: str, href: str) -> rx.Component:
    return rx.chakra.button(
        rx.chakra.link(
            title,
            color=Color.CONTENT.value,
            href=href,
            style={':hover': {'color': '#808080', 'background-color': 'transparent'}},
        )
    )
        