import flet as ft

def signup(page: ft.Page):
    
    page.title = "Registro - Sistema de Reservas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLACK
    
    
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
                alignment=ft.alignment.center  # Centrar el logo
            ),
            
            
            ft.Container(
                content=ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Nombre Completo",
                    border_color=ft.Colors.BLUE,
                    prefix_icon=ft.Icons.PERSON
                ),
                padding=ft.padding.only(15, 10),
                alignment=ft.alignment.center
            ),
            
            ft.Container(
                content=ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Telefono",
                    border_color=ft.Colors.BLUE,
                    prefix_icon=ft.Icons.PHONE
                ),
                padding=ft.padding.only(15, 10),
                alignment=ft.alignment.center
            ),

            ft.Container(
                content=ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Dirección",
                    border_color=ft.Colors.BLUE,
                    prefix_icon=ft.Icons.HOUSE
                ),
                padding=ft.padding.only(15, 10),
                alignment=ft.alignment.center
            ),
            
            
            
            ft.Container(
                content=ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Correo Electrónico",
                    border_color=ft.Colors.BLUE,
                    prefix_icon=ft.Icons.EMAIL
                ),
                padding=ft.padding.only(15, 10),
                alignment=ft.alignment.center
            ),
            
            
            ft.Container(
                content=ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Contraseña",
                    border_color=ft.Colors.BLUE,
                    prefix_icon=ft.Icons.LOCK,
                    password=True,
                    can_reveal_password=True,
                ),
                padding=ft.padding.only(15, 10),
                alignment=ft.alignment.center
            ),
        
            # Botón de Registro
            ft.Container(
                content=ft.ElevatedButton(
                    text="Crear Cuenta",
                    width=280,
                    height=40,
                    bgcolor=ft.Colors.BLUE,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: print("Cuenta creada exitosamente")
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
        height=580,  # Altura mayor para más campos
        bgcolor=ft.Colors.BLACK,  # Fondo negro sólido
        alignment=ft.alignment.center  # Centrar todo el contenido del contenedor
    )
    
    # Agregar el contenedor centrado en la página
    page.add(
        ft.Container(
            content=registro_container,
            alignment=ft.alignment.center,
            expand=True
        )
    )

# Ejecutar la aplicación
if __name__ == "__main__":
    print("🌐 Iniciando página de registro...")
    print("📱 Ve a: http://localhost:8081")
    print("🖼️ Logo: logo_forja.jpg cargado")
    print("🔄 Para ver cambios: Para servidor (Ctrl+C) y reinicia")
    
    ft.app(
        target=signup, 
        view=ft.WEB_BROWSER,
        port=8081,
        assets_dir="assets"
    )