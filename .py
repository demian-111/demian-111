import flet as ft


def main(page: ft.Page):
    page.title="Galeria"
    page.bgcolor=ft.Colors.BLACK45
    
    pinturas = [
        {
            "titulo": "El viento se levanta",
            "autor": "Hayao Miyazaki",
            "año": 2013,
            "descripcion": "pareja al aire libre, en un entorno natural bajo un cielo azul con algunas nubes",
            "imagen": ""
        },
        {
            "titulo": "",
            "autor": "",
            "año": ,
            "descripcion": "",
            "imagen": ""
            },
        { 
         "titulo": "",
            "autor": "",
            "año": ,
            "descripcion": "",
            "imagen": ""
            },
        {
            "titulo": "",
            "autor": "",
            "año": ,
            "descripcion": "",
            "imagen": ""
            },
        { 
         "titulo": "",
            "autor": "",
            "año": ,
            "descripcion": "",
            "imagen": ""
            },
        { 
         "titulo": "",
            "autor": "",
            "año": ,
            "descripcion": "",
            "imagen": ""
            },
        { 
         "titulo": "",
            "autor": "",
            "año": ,
            "descripcion": "",
            "imagen": ""
            },
        { 
         "titulo": "",
            "autor": "",
            "año": ,
            "descripcion": "",
            "imagen": ""
            },
        { 
         "titulo": "",
            "autor": "",
            "año": ,
            "descripcion": "",
            "imagen": ""
            },
        { 
         "titulo": "",
            "autor": "",
            "año": ,
            "descripcion": "",
            "imagen": ""
            },
    ]
    
    indice_actual=[0]
    
    contenedor=ft.Container(
        content=ft.Column([]),
        width=400,
        height=500,
        bgcolor=ft.Colors.BLUE_400,
        alignment=ft.alignment.center
    )
