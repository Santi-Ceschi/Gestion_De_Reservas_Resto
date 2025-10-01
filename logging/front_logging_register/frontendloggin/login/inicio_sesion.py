import flet as ft

def main(page: ft.Page):
    
    page.title = "Login - Sistema de Reservas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.SURFACE_VARIANT
    
    
    login_container = ft.Container(
        content=ft.Column([
            
            ft.Container(
                content=ft.Image(
                    src="/logo_forja.jpg",  # Ruta desde assets_dir (directorio actual)
                    width=300,  # Ancho del logo
                    height=120,  # Alto del logo
                    fit=ft.ImageFit.CONTAIN  # Para mantener proporciones
                ),
                padding=ft.padding.only(top=20, bottom=20),
                alignment=ft.alignment.center  # Centrar el logo
            ),
            
            
            ft.Container(
                content=ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Correo Electrónico",
                    border_color=ft.colors.BLUE,
                    prefix_icon=ft.icons.EMAIL
                ),
                padding=ft.padding.only(20, 20)
            ),
            
            
            ft.Container(
                content=ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Contraseña",
                    border_color=ft.colors.BLUE,
                    prefix_icon=ft.icons.LOCK,
                    password=True
                ),
                padding=ft.padding.only(20, 20)
            ),
            
        
            ft.Container(
                content=ft.ElevatedButton(
                    text="Iniciar Sesión",
                    width=280,
                    height=40,
                    bgcolor=ft.colors.BLUE,
                    color=ft.colors.WHITE
                ),
                padding=ft.padding.only(20, 20)
            ),
            
            ft.Container(
                content=ft.Column([
                    ft.TextButton(
                        text="¿No tienes una cuenta? Regístrate",
                        on_click=lambda e: print("Ir a registro")
                    ),
                ], 
                spacing=5,  # Espacio pequeño entre los botones
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=ft.padding.only(top=10, bottom=10),  # Menos padding
                alignment=ft.alignment.center 
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        
        border_radius=20,
        width=320,
        height=500,
        bgcolor=ft.colors.BLACK  # Fondo negro sólido
    )
    
    page.add(login_container)

# Ejecutar la aplicación
if __name__ == "__main__":
    print("🌐 Iniciando login en página web...")
    print("📱 Ve a: http://localhost:8080")
    print("🖼️ Logo: logo_forja.jpg cargado")
    print("🔄 Para ver cambios: Para servidor (Ctrl+C) y reinicia")
    
    ft.app(
        target=main, 
        view=ft.WEB_BROWSER,
        port=8080,  # Cambiado a puerto 8080
        web_renderer=ft.WebRenderer.HTML,
        assets_dir="."  # Directorio actual como assets
    )