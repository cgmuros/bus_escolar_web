import reflex as rx
import requests
from school_bus_app.routes import Route
from school_bus_app.states.parents_state import ParentsState





class NavbarState(rx.State):
    token: str = ParentsState.id_token_json


    async def is_logged_in(self):
        if ParentsState.id_token_json != "" or ParentsState.id_token_json != None:
            return True
        else:
            return False
