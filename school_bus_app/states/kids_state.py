from typing import Any
import reflex as rx
from school_bus_app.routes import Route
from school_bus_app.states.parents_state import ParentsState





class KidsState(rx.State):
    clicked_data: str = "Cell clicked: "

    cols: list[Any] = [
        {"title": "Title", "type": "str"},
        {
            "title": "Name",
            "type": "str",
            "group": "Data",
            "width": 300,
        },
        {
            "title": "Birth",
            "type": "str",
            "group": "Data",
            "width": 150,
        },
        {
            "title": "Human",
            "type": "bool",
            "group": "Data",
            "width": 80,
        },
        {
            "title": "House",
            "type": "str",
            "group": "Data",
        },
        {
            "title": "Wand",
            "type": "str",
            "group": "Data",
            "width": 250,
        },
        {
            "title": "Patronus",
            "type": "str",
            "group": "Data",
        },
        {
            "title": "Blood status",
            "type": "str",
            "group": "Data",
            "width": 200,
        },
    ]

    data = [
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11'  Holly  phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3",
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "10¾'  vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "4",
            "Albus Percival Wulfric Brian Dumbledore",
            "Late August 1881",
            True,
            "Gryffindor",
            "15' Elder Thestral tail hair core",
            "Phoenix",
            "Half-blood",
        ],
        [
            "5",
            "Rubeus Hagrid",
            "6 December 1928",
            False,
            "Gryffindor",
            "16'  Oak unknown core",
            "None",
            "Part-Human (Half-giant)",
        ],
        [
            "6",
            "Fred Weasley",
            "1 April, 1978",
            True,
            "Gryffindor",
            "Unknown",
            "Unknown",
            "Pure-blood",
        ],
    ]

    def click_cell(self, pos):
        col, row = pos
        yield self.get_clicked_data(pos)

    def get_clicked_data(self, pos) -> str:
        self.clicked_data = f"Cell clicked: {pos}"