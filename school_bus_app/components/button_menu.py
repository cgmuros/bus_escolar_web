import reflex as rx
from typing import Any
from school_bus_app.styles.colors import Color



def button_menu(title: str, href: str) -> rx.Component:
    return rx.chakra.button(
        rx.chakra.link(
            title,
            color=Color.CONTENT.value,
            href=href,
            style={':hover': {'color': '#808080', 'background-color': 'transparent'}},
        )
    )
        