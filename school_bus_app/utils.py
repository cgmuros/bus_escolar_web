import reflex as rx

# Common
index_title = "Aqui esta el Bus Escolar. Gestion de Buses Escolares"
index_description = "implementando soluciones de Chile para el mundo"
preview = "me_128.png"
meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": index_title},
        {"name": "og:description", "content": index_description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@cmurosdev"}
    ]

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang = 'es'")

