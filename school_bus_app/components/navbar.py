import reflex as rx
import school_bus_app.styles.styles as styles
from school_bus_app.styles.colors import Color
from school_bus_app.styles.styles import Size




def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.box(
            rx.chakra.hstack(
                rx.chakra.link(
                    rx.chakra.image(src="/logo.png", width="128px"),
                    href="/",  
                ),
                rx.chakra.span("School ", color=Color.PRIMARY.value),
                rx.chakra.span("Bus", color=Color.PRIMARY.value),
            ),
            style=styles.navbar_title_style
        ),
        rx.chakra.center(
            rx.chakra.hstack(
                rx.chakra.link(
                    rx.chakra.center(
                        rx.chakra.button(
                        "Padres", 
                        color=Color.SECONDARY.value, 
                        variant="unstyled", 
                        style={':hover': {'color': '#d3d3d3'}}
                        )
                    ),
                    href="/parents",
                    is_external=False,
                ),
                rx.chakra.spacer(),
                rx.chakra.center(rx.text("Conductores", color=Color.SECONDARY.value)),
                rx.chakra.spacer(),
                rx.chakra.center(rx.text("Colegios", color=Color.SECONDARY.value)),
                rx.chakra.spacer(),
                rx.chakra.center(rx.text("Soluciones", color=Color.SECONDARY.value)),
                rx.chakra.spacer(),
                rx.chakra.center(rx.text("Nosotros", color=Color.SECONDARY.value))
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