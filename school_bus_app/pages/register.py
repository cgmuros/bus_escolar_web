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
    return rx.box(
        navbar(),
        rx.container(
            rx.form(
                rx.vstack(
                    rx.text("Nombre"),
                    rx.input(placeholder="Nombre", name="first_name"),
                    rx.text("Apellido"),
                    rx.input(placeholder="Apellido", name="last_name"),
                    rx.text("Usuario"),
                    rx.input(placeholder="Username", name="username"),
                    rx.text("Correo"),
                    rx.input(placeholder="Correo", name="email"),
                    rx.text("Contraseña"),
                    rx.password(placeholder="Contraseña", name="hashed_password"),
                    rx.text("Repetir Contraseña"),
                    rx.password(placeholder="Repetir Contraseña", name="password"),
                    rx.text("Telefono"),
                    rx.input(placeholder="Telefono", name="phone_number"),
                    rx.text("Pais"),
                    rx.input(placeholder="Pais", name="country"),
                    rx.text("Region"),
                    rx.input(placeholder="Region", name="region"),
                    rx.text("Ciudad"),
                    rx.input(placeholder="Ciudad", name="city"),
                    rx.button("Registrarse", variant="solid", color=Color.CONTENT.value),
                    align_items="left"
                ),
            ),
            margin_top=Size.VERY_BIG.value,
        ),
    )