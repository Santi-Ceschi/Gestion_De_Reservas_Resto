import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Gestión de Usuarios - La Forja"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = ft.Colors.WHITE
    page.window_width = 1200
    page.window_height = 800
    page.scroll = ft.ScrollMode.AUTO
    
    # Variables de estado
    usuarios_lista = [
        {"id": 1, "nombre": "Juan Pérez", "email": "juan@email.com", "telefono": "123-456-789"},
        {"id": 2, "nombre": "María García", "email": "maria@email.com", "telefono": "987-654-321"},
        {"id": 3, "nombre": "Carlos López", "email": "carlos@email.com", "telefono": "555-123-456"},
    ]
    
    # Crear el header (similar al del proyecto principal)
    header = ft.Container(
        content=ft.Row([
            ft.Row([
                ft.Text("🍽️", size=30),
                ft.Text(
                    "La Forja - Gestión de Usuarios",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                )
            ], spacing=10),
            ft.Row([
                ft.ElevatedButton(
                    "Volver al Inicio",
                    bgcolor=ft.Colors.ORANGE_600,
                    color=ft.Colors.WHITE,
                    icon=ft.Icons.HOME
                ),
                ft.ElevatedButton(
                    "Cerrar Sesión",
                    bgcolor=ft.Colors.RED_600,
                    color=ft.Colors.WHITE,
                    icon=ft.Icons.LOGOUT,
                    on_click=lambda e: cerrar_sesion()
                )
            ], spacing=10)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=ft.padding.symmetric(horizontal=50, vertical=20),
        bgcolor=ft.Colors.BLACK,
        height=80
    )
    
    # Función para cerrar sesión
    def cerrar_sesion():
        page.show_snack_bar(
            ft.SnackBar(
                content=ft.Text("Sesión cerrada correctamente"),
                bgcolor=ft.Colors.GREEN_600
            )
        )
    
    # Función para eliminar usuario
    def eliminar_usuario(usuario_id):
        global usuarios_lista
        usuarios_lista = [u for u in usuarios_lista if u["id"] != usuario_id]
        actualizar_lista_usuarios()
        page.show_snack_bar(
            ft.SnackBar(
                content=ft.Text(f"Usuario eliminado correctamente"),
                bgcolor=ft.Colors.RED_600
            )
        )
    
    # Función para mostrar diálogo de edición
    def mostrar_editar_usuario(usuario):
        nombre_field = ft.TextField(
            label="Nombre completo",
            value=usuario["nombre"],
            width=300
        )
        email_field = ft.TextField(
            label="Email",
            value=usuario["email"],
            width=300
        )
        telefono_field = ft.TextField(
            label="Teléfono",
            value=usuario["telefono"],
            width=300
        )
        
        def guardar_cambios(e):
            # Actualizar usuario en la lista
            for u in usuarios_lista:
                if u["id"] == usuario["id"]:
                    u["nombre"] = nombre_field.value
                    u["email"] = email_field.value
                    u["telefono"] = telefono_field.value
                    break
            
            actualizar_lista_usuarios()
            page.close(dialog)
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Usuario actualizado correctamente"),
                    bgcolor=ft.Colors.GREEN_600
                )
            )
        
        dialog = ft.AlertDialog(
            title=ft.Text("Editar Usuario"),
            content=ft.Column([
                nombre_field,
                email_field,
                telefono_field
            ], spacing=15, tight=True),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: page.close(dialog)),
                ft.ElevatedButton(
                    "Guardar",
                    bgcolor=ft.Colors.GREEN_600,
                    color=ft.Colors.WHITE,
                    on_click=guardar_cambios
                )
            ]
        )
        page.open(dialog)
    
    # Función para confirmar eliminación
    def confirmar_eliminacion(usuario):
        dialog = ft.AlertDialog(
            title=ft.Text("Confirmar Eliminación"),
            content=ft.Text(f"¿Estás seguro de que quieres eliminar al usuario '{usuario['nombre']}'?"),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: page.close(dialog)),
                ft.ElevatedButton(
                    "Eliminar",
                    bgcolor=ft.Colors.RED_600,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: [eliminar_usuario(usuario["id"]), page.close(dialog)]
                )
            ]
        )
        page.open(dialog)
    
    # Crear tarjeta de usuario
    def crear_tarjeta_usuario(usuario):
        return ft.Container(
            content=ft.Row([
                # Información del usuario
                ft.Column([
                    ft.Text(
                        usuario["nombre"],
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BROWN_800
                    ),
                    ft.Text(
                        f"📧 {usuario['email']}",
                        size=14,
                        color=ft.Colors.BROWN_600
                    ),
                    ft.Text(
                        f"📞 {usuario['telefono']}",
                        size=14,
                        color=ft.Colors.BROWN_600
                    )
                ], spacing=5, expand=True),
                
                # Botones de acción
                ft.Row([
                    ft.ElevatedButton(
                        "Editar",
                        bgcolor=ft.Colors.BLUE_600,
                        color=ft.Colors.WHITE,
                        icon=ft.Icons.EDIT,
                        on_click=lambda e: mostrar_editar_usuario(usuario)
                    ),
                    ft.ElevatedButton(
                        "Eliminar",
                        bgcolor=ft.Colors.RED_600,
                        color=ft.Colors.WHITE,
                        icon=ft.Icons.DELETE,
                        on_click=lambda e: confirmar_eliminacion(usuario)
                    )
                ], spacing=10)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=20,
            margin=10,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=8,
                color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
                offset=ft.Offset(2, 2)
            )
        )
    
    # Container para la lista de usuarios
    lista_usuarios_container = ft.Column(spacing=10)
    
    # Función para actualizar la lista de usuarios
    def actualizar_lista_usuarios():
        lista_usuarios_container.controls.clear()
        for usuario in usuarios_lista:
            lista_usuarios_container.controls.append(crear_tarjeta_usuario(usuario))
        page.update()
    
    # Contenido principal
    main_content = ft.Container(
        content=ft.Column([
            # Título de la sección
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Gestión de Usuarios",
                        size=36,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BROWN_800,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Administra los usuarios del sistema de reservas",
                        size=18,
                        color=ft.Colors.BROWN_600,
                        text_align=ft.TextAlign.CENTER
                    )
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40,
                bgcolor=ft.Colors.WHITE
            ),
            
            # Lista de usuarios
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        f"Total de usuarios: {len(usuarios_lista)}",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BROWN_800
                    ),
                    ft.Divider(color=ft.Colors.BROWN_300),
                    lista_usuarios_container
                ], spacing=20),
                padding=50
            )
        ], spacing=0),
        expand=True
    )
    
    # Footer (consistente con el proyecto)
    footer = ft.Container(
        content=ft.Row([
            ft.Column([
                ft.Text("La Forja", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text("© 2025 Sistema de Gestión", size=12, color=ft.Colors.WHITE70)
            ]),
            ft.Column([
                ft.Text("Soporte", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text("📞 +54 11 1234-5678", size=12, color=ft.Colors.WHITE70)
            ]),
            ft.Column([
                ft.Text("Admin Panel", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text("Gestión de usuarios", size=12, color=ft.Colors.WHITE70)
            ])
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
        padding=30,
        bgcolor=ft.Colors.BROWN_800,
        height=120
    )
    
    # Inicializar la lista de usuarios
    actualizar_lista_usuarios()
    
    # Estructura principal con footer fijo
    page.add(
        ft.Stack([
            # Contenido principal con scroll
            ft.Container(
                content=ft.ListView([
                    header,
                    main_content,
                    ft.Container(height=120)  # Espacio para el footer fijo
                ], spacing=0),
                expand=True
            ),
            # Footer fijo
            ft.Container(
                content=footer,
                alignment=ft.alignment.bottom_center,
                bottom=0,
                left=0,
                right=0
            )
        ])
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=8084)