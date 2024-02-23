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
                        rx.chakra.text("Usuario",
                                width="100px",
                                ),
                        rx.chakra.input(placeholder="Usuario", 
                                name="username",
                                # align_items="right",
                                width="200px",
                                # margin_left="50%",
                                 ),
                    ),
                    rx.hstack(
                        rx.chakra.text("Contraseña",
                                width="100px",
                                ),
                        rx.chakra.password(placeholder="Contraseña", 
                                    name="password",
                                    width="200px",
                                    ),
                    ),
                    rx.hstack(
                        rx.chakra.button("Ingresar", 
                                  variant="solid", 
                                  color=Color.CONTENT.value, 
                                  type_="submit",
                                  width="120px",
                                  ),
                        rx.chakra.button(
                            rx.link("Registrarse", 
                                  variant="solid", 
                                  color=Color.CONTENT.value,
                                  width="120px",
                                  href=Route.REGISTER.value,),
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