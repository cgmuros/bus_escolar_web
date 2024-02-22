import reflex as rx
import requests
from school_bus_app.routes import Route


class ParentsState(rx.State):
    username: str
    password: str
    id_token_json: str = rx.LocalStorage()


    async def on_load(self):
        if self.id_token_json != "" and self.id_token_json != None:
            return rx.redirect(Route.PARENTS_MAIN.value) 


    async def login(self, form_data: dict):
        username = form_data["username"]
        password = form_data["password"]

        data = {"username": username, "password": password}
        response = requests.post(
            "http://localhost:8000/auth/",
            data=data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'})

        if response.status_code == 200:
            token = response.json() 
            if token:
                self.id_token_json = token
                return rx.redirect(Route.PARENTS_MAIN.value)
        else:
            self.id_token_json = ""
            return rx.window_alert("Usuario o contraseña incorrectos")


    async def get_username_from_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'access_token': self.id_token_json
        }

        response = requests.post(
            "http://localhost:8000/auth/me/",
            headers=headers
        )

        if  response.status_code != 200:
            self.id_token_json = ""
            return rx.redirect(Route.PARENTS.value)
        try:
            response_json = response.json()
            self.username = response_json["username"]
            return None
        except ValueError:
            print("Invalid JSON response")
            self.id_token_json = ""
            return rx.redirect(Route.PARENTS.value)
        except:
            self.id_token_json = ""
            return rx.redirect(Route.PARENTS.value)

    async def logout(self):
        self.id_token_json = ""
        return rx.redirect(Route.PARENTS.value)