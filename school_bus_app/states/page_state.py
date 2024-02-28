import reflex as rx
import requests
from school_bus_app.routes import Route
from school_bus_app.constants import Constants



class PageState(rx.State):
    username: str
    password: str
    id_token_json: str = rx.LocalStorage(name="id_token_json")

    countries: list[str] = []
    regions: list[str] = []
    cities: list[str] = []
    email: str = ""
    phone_number: str = ""

    countries_combo: list[str] = []
    regions_combo: list[str] = []
    cities_combo: list[str] = []


    def get_countries(self):
        response_countries = requests.get(
            f"{Constants.ENDPOINT_COUNTRY.value}/",
            )
        
        if response_countries.status_code == 200:
            return response_countries
        else:
            return None


    def get_about_me(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'access_token': self.id_token_json
        }

        response = requests.get(
            f"{Constants.ENDPOINT_USER.value}/",
            headers=headers
        )


        if response.status_code == 200:
            return response
        else:
            return None


    async def validate_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'access_token': self.id_token_json
        }

        response = requests.post(
            f"{Constants.ENDPOINT_AUTH.value}/me/",
            headers=headers
        )

        if  response.status_code != 200:
            await self.logout()

        try:
            response_json = response.json()
            self.username = response_json["username"]
            return None
        except ValueError:
            print("Invalid JSON response")
            return await self.logout()
        except:
            return await self.logout()
        

    async def on_load(self):
        if self.id_token_json != "" and self.id_token_json != None:
            return rx.redirect(Route.PARENTS_MAIN.value) 


    async def on_load_new_student(self):
        
        response_countries = self.get_countries()
        response_me = self.get_about_me()

        if response_countries is not None and response_me is not None:
            self.countries = response_countries.json()
            self.countries_combo  = [item["name"] for item in response_countries.json()]
            self.email = [item["email"] for item in response_me.json()]
            self.phone_number = [item["phone_number"] for item in response_me.json()]
        else:
            return None


    async def login(self, form_data: dict):
        username = form_data["username"]
        password = form_data["password"]

        data = {"username": username, "password": password}
        response = requests.post(
            f"{Constants.ENDPOINT_AUTH.value}/",
            data=data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )

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
            f"{Constants.ENDPOINT_AUTH.value}/me/",
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
    

    async def get_regions_by_country(self, country: str):
        response_region = requests.get(
            f"{Constants.ENDPOINT_REGION.value}/",
            )
        
        if response_region.status_code == 200:
            self.regions = response_region.json()
            country_id = next((item["id"] for item in self.countries if item["name"] == country), None)
            self.regions_combo = [item["name"] for item in response_region.json() if item.get("country_id") == country_id]
        else:
            return None


    async def get_cities_by_region(self, region: str):
        response_city = requests.get(
            f"{Constants.ENDPOINT_CITY.value}/",
            )
        
        if response_city.status_code == 200:
            self.cities = response_city.json()
            region_id = next((item["id"] for item in self.regions if item["name"] == region), None)
            self.cities_combo = [item["name"] for item in response_city.json() if item.get("region_id") == region_id]
        else:
            return None
        

    async def on_load_register(self):
        response_countries = requests.get(
            f"{Constants.ENDPOINT_COUNTRY.value}/",
            )
        
        if response_countries.status_code == 200:
            self.countries = response_countries.json()
            self.countries_combo  = [item["name"] for item in response_countries.json()]
        else:
            return None


    async def get_regions_by_country_register(self, country: str):
        response_region = requests.get(
            f"{Constants.ENDPOINT_REGION.value}/",
            )
        if response_region.status_code == 200:
            self.regions = response_region.json()
            country_id = next((item["id"] for item in self.countries if item["name"] == country), None)
            self.regions_combo = [item["name"] for item in response_region.json() if item.get("country_id") == country_id]
        else:
            return None


    async def get_cities_by_region_register(self, region: str):
        response_city = requests.get(
            f"{Constants.ENDPOINT_CITY.value}/",
            )
        
        if response_city.status_code == 200:
            self.cities = response_city.json()
            region_id = next((item["id"] for item in self.regions if item["name"] == region), None)
            self.cities_combo = [item["name"] for item in response_city.json() if item.get("region_id") == region_id]
        else:
            return None


    async def register(self, form_data: dict):

        form_data["country"] = next((item["id"] for item in self.countries if item["name"] == form_data.get("country")), None)
        form_data["region"] = next((item["id"] for item in self.regions if item["name"] == form_data.get("region")), None)
        form_data["city"] = next((item["id"] for item in self.cities if item["name"] == form_data.get("city")), None)
        # Add parent role
        form_data["role"] = 2

        if form_data["hashed_password"] != form_data["password"]:
            return rx.window_alert("Las contraseñas no coinciden")

        response = requests.post(
            f"{Constants.ENDPOINT_AUTH.value}/register/",
            data=form_data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )

        if response.status_code == 201:
            return rx.window_alert("Usuario registrado con exito")
        