import flet as ft
import requests
import os

token_jwt = None  # Variable global para guardar el token

def main(page: ft.Page):
    page.title = "Registro y Login"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    email_field = ft.TextField(label="Email", width=300)
    password_field = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    nombre_field = ft.TextField(label="Nombre", width=300)
    telefono_field = ft.TextField(label="Teléfono", width=300)
    direccion_field = ft.TextField(label="Dirección", width=300)
    rol_field = ft.TextField(label="Rol", width=300, value="usuario")

    def registrar_usuario(e):
        datos = {
            "nombre": nombre_field.value,
            "email": email_field.value,
            "telefono": telefono_field.value,
            "direccion": direccion_field.value,
            "contrasena": password_field.value,
            "rol": rol_field.value
        }
        respuesta = requests.post("http://localhost:8000/users/register", json=datos)
        try:
            print("Registro:", respuesta.json())
        except Exception:
            print("Registro (no JSON):", respuesta.text)

    def login_usuario(e):
        global token_jwt
        datos = {
            "email": email_field.value,
            "password": password_field.value
        }
        respuesta = requests.post("http://localhost:8000/users/login", json=datos)
        try:
            print("Login:", respuesta.json())
            if respuesta.status_code == 200 and "access_token" in respuesta.json():
                token_jwt = respuesta.json()["access_token"]
                print("Token guardado:", token_jwt)
            else:
                print("No se recibió token JWT")
        except Exception:
            print("Login (no JSON):", respuesta.text)

    def logout_usuario(e):
        global token_jwt
        if token_jwt:
            token_jwt = None
            print("Sesión cerrada. Token eliminado.")
        else:
            print("No hay sesión activa.")

    try:
        logo = ft.Image(src="logo_forja.jpg", width=300, height=120, fit=ft.ImageFit.CONTAIN)
        page.add(ft.Container(content=logo, alignment=ft.alignment.center))
    except Exception as img_error:
        page.add(ft.Text(f"Error cargando imagen: {img_error}", color=ft.colors.RED))

    page.add(
        nombre_field,
        email_field,
        telefono_field,
        direccion_field,
        password_field,
        rol_field,
        ft.ElevatedButton("Registrar", on_click=registrar_usuario),
        ft.ElevatedButton("Login", on_click=login_usuario),
        ft.ElevatedButton("Cerrar sesión", on_click=logout_usuario)
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="../front_logging_register/frontendloggin/login/assets")
