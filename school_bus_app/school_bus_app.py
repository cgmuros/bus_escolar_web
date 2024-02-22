import reflex as rx
import school_bus_app.styles.styles as styles
from school_bus_app.pages.index import index
from school_bus_app.pages.register import register
from school_bus_app.pages.parents_login import parents
from school_bus_app.pages.parents_main import parents_main
from school_bus_app.pages.parents_kids import parents_kids



class State(rx.State):
    """The app state."""
    pass


# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLESCHEETS,
    style=styles.BASE_STYLE
)


