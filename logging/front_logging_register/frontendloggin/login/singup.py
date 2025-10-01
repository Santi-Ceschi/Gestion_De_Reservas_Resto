import flet as ft
import httpx

def signup(page: ft.Page):
    page.title = "Registro - Sistema de Reservas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK

    # 1. Define los campos como variables
    nombre_field = ft.TextField(
        width=280,
        height=40,
        hint_text="Nombre Completo",
        border_color=ft.colors.BLUE,
        prefix_icon=ft.icons.PERSON
    )
    telefono_field = ft.TextField(
        width=280,
        height=40,
        hint_text="Telefono",
        border_color=ft.colors.BLUE,
        prefix_icon=ft.icons.PHONE
    )
    direccion_field = ft.TextField(
        width=280,
        height=40,
        hint_text="Dirección",
        border_color=ft.colors.BLUE,
        prefix_icon=ft.icons.HOUSE
    )
    correo_field = ft.TextField(
        width=280,
        height=40,
        hint_text="Correo Electrónico",
        border_color=ft.colors.BLUE,
        prefix_icon=ft.icons.EMAIL
    )
    contrasena_field = ft.TextField(
        width=280,
        height=40,
        hint_text="Contraseña",
        border_color=ft.colors.BLUE,
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
    )

    # 2. Función para enviar los datos
    def registrar_usuario(e):
        response = httpx.post(
            "http://localhost:8000/users/register",
            json={
                "nombre": nombre_field.value,
                "email": correo_field.value,  # Cambiado de 'correo' a 'email'
                "telefono": telefono_field.value,
                "direccion": direccion_field.value,
                "contrasena": contrasena_field.value,
                "rol": "cliente"  # Agregado campo 'rol'
            }
        )
        if response.status_code == 200:
            print("Cuenta creada exitosamente")
        else:
            print("Error al crear la cuenta")
            print(response.text)  # Muestra el mensaje de error detallado

    registro_container = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Image(
                    src="logo_forja.jpg",
                    width=300,
                    height=120,
                    fit=ft.ImageFit.CONTAIN
                ),
                padding=ft.padding.only(top=15, bottom=15),
                alignment=ft.alignment.center
            ),
            ft.Container(content=nombre_field, padding=ft.padding.only(15, 10), alignment=ft.alignment.center),
            ft.Container(content=telefono_field, padding=ft.padding.only(15, 10), alignment=ft.alignment.center),
            ft.Container(content=direccion_field, padding=ft.padding.only(15, 10), alignment=ft.alignment.center),
            ft.Container(content=correo_field, padding=ft.padding.only(15, 10), alignment=ft.alignment.center),
            ft.Container(content=contrasena_field, padding=ft.padding.only(15, 10), alignment=ft.alignment.center),
            ft.Container(
                content=ft.ElevatedButton(
                    text="Crear Cuenta",
                    width=280,
                    height=40,
                    bgcolor=ft.colors.BLUE,
                    color=ft.colors.WHITE,
                    on_click=registrar_usuario
                ),
                padding=ft.padding.only(15, 15),
                alignment=ft.alignment.center
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        border_radius=20,
        width=320,
        height=580,
        bgcolor=ft.colors.BLACK,
        alignment=ft.alignment.center
    )

    page.add(
        ft.Container(
            content=registro_container,
            alignment=ft.alignment.center,
            expand=True
        )
    )

if __name__ == "__main__":
    print("🌐 Iniciando página de registro...")
    print("📱 Ve a: http://localhost:8081")
    print("🖼️ Logo: logo_forja.jpg cargado")
    print("🔄 Para ver cambios: Para servidor (Ctrl+C) y reinicia")

    ft.app(
        target=signup,
        view=ft.AppView.WEB_BROWSER,
        port=8081,
        assets_dir="assets"
    )
