import flet as ft


def main(page: ft.Page):
    page.title="Galeria"
    page.bgcolor=ft.Colors.BLACK45
    
    pinturas = [
        {
            "titulo": "La Máquina Diferencial",
            "autor": "William Gibson y Bruce Sterling",
            "año": 1822,
            "descripcion": "calculadora mecánica automática diseñada por Charles Babbage a principios del siglo XIX para tabular funciones polinómicas y calcular tablas matemáticas complejas de forma mecánica y precisa",
            "imagen": "https://rescepto.wordpress.com/wp-content/uploads/2019/10/maquina_diferencial.jpg"
        },
        {
            "titulo": "Mortal Engines",
            "autor": "Philip Reeve",
            "año": 2001,
            "descripcion": "es la primera novela de una saga juvenil postapocalíptica donde las ciudades se han transformado en enormes máquinas móviles que vagan por la Tierra devorando a ciudades más pequeñas en busca de recursos para sobrevivir",
            "imagen": "https://m.media-amazon.com/images/I/513F1ugdFjL._SY445_SX342_ML2_.jpg"
            },
        { 
         "titulo": "Las Puertas de Anubis",
            "autor": "Tim Powers",
            "año": 1983,
            "descripcion": "novela de fantasía y ciencia ficción sobre viajes en el tiempo que mezcla elementos históricos con magia y sociedades secretas en el Londres de principios del siglo XIX",
            "imagen": "https://http2.mlstatic.com/D_NQ_NP_707449-MLU77723050893_072024-O.webp"
            },
        {
            "titulo": "La materia oscura ",
            "autor": "Philip Pullman",
            "año": 1995,
            "descripcion": "trilogía de fantasía épica que se desarrolla en universos paralelos y narra la historia de la joven Lyra Belacqua, cuya vida da un vuelco al descubrir el secreto de una partícula misteriosa llamada "Polvo" y la persecución que sufre por parte de una iglesia todopoderosa, el Magisterio, que intenta controlar la conciencia y la inteligencia humana",
            "imagen": "https://www.editorialastronave.com/upload/media/covers/0001/01/thumb_735_covers_big.jpg"
            },
        { 
         "titulo": "La invención de Hugo Cabret",
            "autor": "Brian Selznick",
            "año": 2007,
            "descripcion": "novela que narra la historia de Hugo, un huérfano que vive en una estación de tren de París en los años 30 y cuyo único recuerdo de su padre es un misterioso autómata que intenta reparar para descifrar un mensaje secreto",
            "imagen": "https://m.media-amazon.com/images/I/A1hKLQwm9RL._SL1500_.jpg"
            },
        { 
         "titulo": "Leviathan",
            "autor": "Scott Westerfeld",
            "año": 2009,
            "descripcion": "novela de ficción juvenil del subgénero steampunk ambientada en una Primera Guerra Mundial alternativa donde las potencias europeas se dividen en "Clankers", que usan máquinas de guerra mecánicas, y "Darwinistas", que emplean bestias bioingenierizadas",
            "imagen": "https://m.media-amazon.com/images/I/81G7NM8uG3L._SL1500_.jpg"
            },
        { 
         "titulo": "Boneshaker",
            "autor": "Cherie Priest",
            "año": 2009,
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
    
    boton_siguiente=
