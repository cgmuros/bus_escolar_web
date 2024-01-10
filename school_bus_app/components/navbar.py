import reflex as rx
from school_bus_app.styles.colors import Color
from school_bus_app.styles.styles import Size
import school_bus_app.styles.styles as styles


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.hstack(
                rx.image(src="logo.png", width="128px"),
                rx.span("Donde esta ", color=Color.PRIMARY.value),
                rx.span("El Bus", color=Color.PRIMARY.value),
            ),
            style=styles.navbar_title_style
        ),
        rx.center(
            rx.hstack(
                rx.center(rx.text("Padres", color=Color.SECONDARY.value)),
                rx.spacer(),
                rx.center(rx.text("Conductores", color=Color.SECONDARY.value)),
                rx.spacer(),
                rx.center(rx.text("Colegios", color=Color.SECONDARY.value)),
                rx.spacer(),
                rx.center(rx.text("Soluciones", color=Color.SECONDARY.value)),
                rx.spacer(),
                rx.center(rx.text("Nosotros", color=Color.SECONDARY.value))
            ),
            padding_x=Size.VERY_BIG.value,
            padding_y=Size.VERY_BIG.value,
            align_items="end",
        ),
        justify_content="space-between",
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.VERY_BIG.value,
        z_index="999",
        top="0",
        width="100%"
    )