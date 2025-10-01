import flet as ft

def main(page: ft.Page):
    
    page.title = "Login - Sistema de Reservas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLACK
    
    
    login_container = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Correo Electrónico",
                    border_color=ft.Colors.BLUE,
                    prefix_icon=ft.Icons.EMAIL
                ),
                padding=20
            ),
            
            
            ft.Container(
                content=ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Contraseña",
                    border_color=ft.Colors.BLUE,
                    prefix_icon=ft.Icons.LOCK,
                    password=True
                ),
                padding=20
            ),
            
        
            ft.Container(
                content=ft.ElevatedButton(
                    text="Iniciar Sesión",
                    width=280,
                    height=40,
                    bgcolor=ft.Colors.BLUE,
                    color=ft.Colors.WHITE
                ),
                padding=20
            ),
            
            ft.Container(
                content=ft.Column([
                    ft.TextButton(
                        text="¿No tienes una cuenta? Regístrate",
                        on_click=lambda e: print("Ir a registro")
                    )
                ], 
                spacing=5,  # Espacio pequeño entre los botones
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=10 
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        
        border_radius=20,
        width=320,
        height=500,
        bgcolor=ft.Colors.BLACK  # Fondo negro sólido
    )
    
    page.add(login_container)

# Ejecutar la aplicación
if __name__ == "__main__":
    print("🌐 Iniciando login en página web...")
    print("📱 Ve a: http://localhost:8085")
    print("🖼️ Logo: logo_forja.jpg cargado")
    print("🔄 Para ver cambios: Para servidor (Ctrl+C) y reinicia")
    
    ft.app(
        target=main, 
        view=ft.WEB_BROWSER,
        port=8086,  # Cambiado a puerto 8086
        web_renderer=ft.WEB_BROWSER,
        assets_dir="assets"  # Directorio actual como assets
    )