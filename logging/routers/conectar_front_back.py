import flet as ft
import requests

def registrar_usuario(e):
    datos = {
        "nombre": "Juan",
        "email": "juan@email.com",
        "telefono": "123456789",
        "direccion": "Calle Falsa 123",
        "contrasena": "password",
        "rol": "usuario"
    }
    respuesta = requests.post("http://localhost:8000/users/register", json=datos)
    print("Registro:", respuesta.json())

def login_usuario(e):
    datos = {
        "email": "juan@email.com",
        "contrasena": "password"
    }
    respuesta = requests.post("http://localhost:8000/users/login", json=datos)
    print("Login:", respuesta.json())

def main(page: ft.Page):
    btn_registrar = ft.ElevatedButton("Registrar", on_click=registrar_usuario)
    btn_login = ft.ElevatedButton("Login", on_click=login_usuario)
    page.add(btn_registrar, btn_login)

ft.app(target=main)


