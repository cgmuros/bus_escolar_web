import reflex as rx
import school_bus_app.utils as utils
from school_bus_app.styles.styles import Size
from school_bus_app.styles.colors import Color
from school_bus_app.components.navbar import navbar
from school_bus_app.routes import Route
from school_bus_app.components.navbar import navbar
from school_bus_app.states.page_state import PageState
from school_bus_app.components.menu_left import menu_left






@rx.page(
    route=Route.PARENTS_ADD_STUDENT.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.meta,
    on_load=[PageState.validate_token, PageState.on_load_new_student],
)
def parents_add_students() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.box(
            rx.hstack(
                rx.chakra.box(
                    menu_left(),
                    width="25%",
                    padding=Size.SMALL.value,
                ),
                rx.chakra.box(
                    rx.chakra.box(
                        rx.link(
                            rx.chakra.text("Volver"),
                            href=Route.PARENTS_KIDS.value,
                        ),
                    ),
                    rx.chakra.box(
                        rx.form(
                            rx.chakra.vstack(
                                rx.chakra.vstack(
                                    rx.chakra.text("Rut"),
                                    rx.chakra.input(placeholder="Rut", name="rut"),
                                    rx.chakra.text("Nombre"),
                                    rx.chakra.input(placeholder="Nombre", name="first_name"),
                                    rx.chakra.text("Apellido"),
                                    rx.chakra.input(placeholder="Apellido", name="last_name"),
                                    rx.chakra.text("Direccion"),
                                    rx.chakra.input(placeholder="Direccion", name="address"),
                                    rx.chakra.text("Correo Electronico"),
                                    rx.chakra.input(placeholder="Correo", name="email", value=PageState.email),
                                    rx.chakra.text("Celular"),
                                    rx.chakra.input(placeholder="+56 9 ", name="phone_number", value=PageState.phone_number),
                                    rx.chakra.text("Pais"),
                                    rx.select(PageState.countries_combo, 
                                            placeholder="Pais", 
                                            name="country", 
                                            disabled=False,
                                            on_change=lambda value: PageState.get_regions_by_country(value),
                                            ),
                                    rx.chakra.text("Region"),
                                    rx.select(PageState.regions_combo,
                                            placeholder="Region", 
                                            name="region",
                                            on_change=lambda value: PageState.get_cities_by_region(value),
                                            ),
                                    rx.chakra.text("Ciudad"),
                                    rx.select(PageState.cities_combo,
                                        placeholder="Ciudad", 
                                        name="city"
                                        ),
                                    rx.chakra.text("Colegio"),
                                    rx.chakra.input(placeholder="Colegio", name="school"),
                                    rx.chakra.text("Padre"),
                                    rx.chakra.input(placeholder="Padre", name="parent"),
                                    rx.chakra.text("Fecha de Nacimiento"),
                                    rx.chakra.date_picker(placeholder="Fecha Nacimiento", name="birth_date"),
                                    rx.chakra.button("Registrarse", 
                                                    variant="solid", 
                                                    color=Color.CONTENT.value,
                                                    type_="submit",
                                                    ),
                                    align_items="left",
                                    width="50%",
                                ),
                            ),
                            # on_submit=RegisterState.register,
                        ),
                        width="100%",
                    ),
                    width="75%",
                ),
            ),
            max_width="100%",
        ),
    )