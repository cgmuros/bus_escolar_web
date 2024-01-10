import reflex as rx
import school_bus_app.styles.styles as styles
from school_bus_app.styles.styles import Size
from school_bus_app.styles.colors import Color
from school_bus_app.components.navbar import navbar



class State(rx.State):
    """The app state."""
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.hstack(
            rx.vstack(
                rx.text(
                    "Seguridad para sus hijos", 
                    font_size=Size.BIG.value, 
                    color=Color.CONTENT.value, 
                    width="100%",
                    font_weight="bold"),
                rx.text(
                    """
                    Las mañanas son un momento agitado. 
                    Prepararse para ir a trabajar. Preparar a los 
                    niños para ir a la escuela. ¿Y qué tal si, 
                    al menos en lo que respecta a que sus hijos 
                    lleguen al autobús a tiempo, usted pudiera 
                    deshacerse de parte de ese estrés?
                    """
                ),
                bg=Color.PRIMARY.value,
                font_size=Size.LARGE.value,
                padding=Size.VERY_BIG.value,
                width="100%",
                # margin=Size.SMALL.value,
                
            ),
            rx.vstack(
                rx.button("COMENZAR", 
                          variant="solid",
                          color=Color.CONTENT.value,
                          font_size=Size.VERY_BIG.value,
                          padding=Size.MEDIUM.value,
                          width="60%",
                          style={
                            'border': '4px solid black',
                            'background': 'transparent',
                            'border-radius': '20px'
                            }
                        ),
                rx.hstack(
                    rx.image(src="apple.png"),
                    rx.image(src="android.png"),
                ),
                # bg=Color.SECONDARY.value,

                # padding=Size.SMALL.value,
                width="100%",
            ),
            widht="100%",
        ),
    )


# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLESCHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index,
             title="Donde esta el Bus App. Gestion de Buses Escolares")
app.compile()
