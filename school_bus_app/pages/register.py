import reflex as rx
import school_bus_app.utils as utils
from school_bus_app.routes import Route
from school_bus_app.components.navbar import navbar
from school_bus_app.styles.colors import Color
from school_bus_app.styles.styles import Size



class RegisterState(rx.State):
    text: str

    def test(self):
        self.text = "probandooooo"

@rx.page(
    route=Route.REGISTER.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.meta
)
def register() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.container(
            rx.chakra.form(
                rx.chakra.vstack(
                    rx.chakra.text("Nombre"),
                    rx.chakra.input(placeholder="Nombre", name="first_name"),
                    rx.chakra.text("Apellido"),
                    rx.chakra.input(placeholder="Apellido", name="last_name"),
                    rx.chakra.text("Usuario"),
                    rx.chakra.input(placeholder="Username", name="username"),
                    rx.chakra.text("Correo"),
                    rx.chakra.input(placeholder="Correo", name="email"),
                    rx.chakra.text("Contraseña"),
                    rx.chakra.password(placeholder="Contraseña", name="hashed_password"),
                    rx.chakra.text("Repetir Contraseña"),
                    rx.chakra.password(placeholder="Repetir Contraseña", name="password"),
                    rx.chakra.text("Telefono"),
                    rx.chakra.input(placeholder="Telefono", name="phone_number"),
                    rx.chakra.text("Pais"),
                    rx.chakra.input(placeholder="Pais", name="country"),
                    rx.chakra.text("Region"),
                    rx.chakra.input(placeholder="Region", name="region"),
                    rx.chakra.text("Ciudad"),
                    rx.chakra.input(placeholder="Ciudad", name="city"),
                    rx.chakra.button("Registrarse", variant="solid", color=Color.CONTENT.value),
                    align_items="left"
                ),
            ),
            margin_top=Size.VERY_BIG.value,
        ),
    )