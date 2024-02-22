import reflex as rx
import school_bus_app.utils as utils
from school_bus_app.styles.styles import Size
from school_bus_app.styles.colors import Color
from school_bus_app.components.navbar import navbar
from school_bus_app.routes import Route
from school_bus_app.components.navbar import navbar
from school_bus_app.states.parents_state import ParentsState



@rx.page(
    route=Route.PARENTS.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.meta,
    on_load=ParentsState.on_load,
)
def parents() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.form(
                rx.vstack(
                    rx.hstack(
                        rx.text("Usuario",
                                width="100px",
                                ),
                        rx.input(placeholder="Usuario", 
                                name="username",
                                # align_items="right",
                                width="200px",
                                # margin_left="50%",
                                 ),
                    ),
                    rx.hstack(
                        rx.text("Contraseña",
                                width="100px",
                                ),
                        rx.password(placeholder="Contraseña", 
                                    name="password",
                                    width="200px",
                                    ),
                    ),
                    rx.hstack(
                        rx.button("Ingresar", 
                                  variant="solid", 
                                  color=Color.CONTENT.value, 
                                  type_="submit",
                                  width="120px",
                                  ),
                        rx.button("Registrarse", 
                                  variant="solid", 
                                  color=Color.CONTENT.value,
                                  width="120px",
                                  ),
                        padding_top=Size.BIG.value,
                    ),
                    align_items="center",
                ),  
                on_submit=ParentsState.login,
            ),
            padding=Size.VERY_BIG.value,
        ),
    )