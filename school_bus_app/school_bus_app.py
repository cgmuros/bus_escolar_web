import reflex as rx
import school_bus_app.styles.styles as styles
from school_bus_app.pages.index import index
from school_bus_app.pages.register import register
from school_bus_app.pages.parents_login import parents
from school_bus_app.pages.parents_main import parents_main
from school_bus_app.pages.parents_students import parents_students
from school_bus_app.pages.parents_add_student import parents_add_students



class State(rx.State):
    """The app state."""
    pass


# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLESCHEETS,
    style=styles.BASE_STYLE
)


