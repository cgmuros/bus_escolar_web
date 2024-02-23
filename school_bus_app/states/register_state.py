import reflex as rx
import requests
from school_bus_app.states.parents_state import ParentsState


class RegisterState(rx.State):
    countries: list[str] = []
    regions: list[str] = []

    countries_combo: list[str] = []
    regions_combo: list[str] = []


    async def on_load(self):

        response_countries = requests.get("http://localhost:8000/country/")
        if response_countries.status_code == 200:
            self.countries = response_countries.json()
            self.countries_combo  = [item["name"] for item in response_countries.json()]
        else:
            return None

    async def get_regions_by_country(self, country: str):
        response_region = requests.get("http://localhost:8000/region/")
        if response_region.status_code == 200:
            self.regions = response_region.json()
            country_id = next((item["id"] for item in self.countries if item["name"] == country), None)
            self.regions_combo = [item["name"] for item in response_region.json() if item.get("country_id") == country_id]
        else:
            return None

