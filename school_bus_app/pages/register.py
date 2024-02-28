import reflex as rx
import school_bus_app.utils as utils
from school_bus_app.routes import Route
from school_bus_app.components.navbar import navbar
from school_bus_app.styles.colors import Color
from school_bus_app.styles.styles import Size
from school_bus_app.states.page_state import PageState





@rx.page(
    route=Route.REGISTER.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.meta,
    on_load=PageState.on_load_register,
)
def register() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.container(
            rx.chakra.form(
                rx.chakra.vstack(
                    rx.chakra.box(
                        rx.chakra.text("Registro para Padres", 
                                align_items="flex-start",
                                align_content="flex-start",
                                ),
                        width="30%",
                        padding_bottom=Size.BIG.value,
                    ),
                    rx.chakra.vstack(
                        rx.chakra.text("Nombre"),
                        rx.chakra.input(placeholder="Nombre", name="first_name"),
                        rx.chakra.text("Apellido"),
                        rx.chakra.input(placeholder="Apellido", name="last_name"),
                        rx.chakra.text("Usuario"),
                        rx.chakra.input(placeholder="Username", name="username"),
                        rx.chakra.text("Correo Electronico"),
                        rx.chakra.input(placeholder="Correo", name="email"),
                        rx.chakra.text("Celular"),
                        rx.chakra.input(placeholder="+56 9 ", name="phone_number"),
                        rx.chakra.text("Pais"),
                        rx.select(PageState.countries_combo, 
                                placeholder="Pais", 
                                name="country", 
                                disabled=False,
                                on_change=lambda value: PageState.get_regions_by_country_register(value),
                                ),
                        rx.chakra.text("Region"),
                        rx.select(PageState.regions_combo,
                                placeholder="Region", 
                                name="region",
                                on_change=lambda value: PageState.get_cities_by_region_register(value),
                                ),
                        rx.chakra.text("Ciudad"),
                        rx.select(PageState.cities_combo,
                            placeholder="Ciudad", 
                            name="city"
                            ),
                        rx.chakra.text("Direccion"),
                        rx.chakra.input(placeholder="Direccion", name="address"),
                        rx.chakra.text("Contraseña"),
                        rx.chakra.password(placeholder="Contraseña", name="hashed_password"),
                        rx.chakra.text("Repetir Contraseña"),
                        rx.chakra.password(placeholder="Repetir Contraseña", name="password"),
                        rx.chakra.button("Registrarse", 
                                        variant="solid", 
                                        color=Color.CONTENT.value,
                                        type_="submit",
                                        ),
                        align_items="left",
                        width="70%",
                        padding_bottom=Size.BIG.value,
                    ),
                ),
                
                on_submit=PageState.register,
            ),
            margin_top=Size.VERY_BIG.value,
        ),
    )