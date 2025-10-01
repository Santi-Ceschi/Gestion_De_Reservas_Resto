import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Forja - Sistema de Reservas"
    page.bgcolor = ft.Colors.WHITE  # Marrón - usando ft.colors
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO  # Hacer toda la página scrolleable
    
    # Lista para almacenar las reservas (temporal)
    reservas_list = []
    
    # Función para crear reserva
    def crear_reserva(e):
        nombre = nombre_field.value
        telefono = telefono_field.value
        fecha = fecha_field.value
        hora = hora_field.value
        personas = personas_field.value

        if all([nombre, telefono, fecha, hora, personas]):
            nueva_reserva = {
                "id": len(reservas_list) + 1,
                "nombre": nombre,
                "telefono": telefono,
                "fecha": fecha,
                "hora": hora,
                "personas": personas,
                "comentarios": "Sin comentarios",
                "estado": "Confirmada"
            }
            
            reservas_list.append(nueva_reserva)
            
            # Limpiar campos
            nombre_field.value = ""
            telefono_field.value = ""
            fecha_field.value = ""
            hora_field.value = ""
            personas_field.value = ""            
            # Actualizar la lista
            actualizar_lista()
            
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("✅ Reserva creada exitosamente", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.GREEN
                )
            )
            page.update()
        else:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("❌ Completa todos los campos", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.RED
                )
            )
            page.update()
    
    def cancelar_reserva(reserva):
        def on_cancel(e):
            reservas_list.remove(reserva)
            actualizar_lista()
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("🗑️ Reserva cancelada", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.ORANGE
                )
            )
        return on_cancel
    
    def editar_reserva(reserva):
        def on_edit(e):
            # Campos del diálogo de edición
            edit_nombre = ft.TextField(label="Nombre completo", value=reserva['nombre'], width=300)
            edit_telefono = ft.TextField(label="Teléfono", value=reserva['telefono'], width=300)
            edit_fecha = ft.TextField(label="Fecha (DD/MM/YYYY)", value=reserva['fecha'], width=300)
            edit_hora = ft.TextField(label="Hora (HH:MM)", value=reserva['hora'], width=300)
            edit_personas = ft.TextField(label="Número de personas", value=reserva['personas'], width=300)
            
            def guardar_cambios(e):
                if all([edit_nombre.value, edit_telefono.value, edit_fecha.value, edit_hora.value, edit_personas.value]):
                    # Actualizar la reserva
                    reserva['nombre'] = edit_nombre.value
                    reserva['telefono'] = edit_telefono.value
                    reserva['fecha'] = edit_fecha.value
                    reserva['hora'] = edit_hora.value
                    reserva['personas'] = edit_personas.value
                    
                    # Actualizar la lista
                    actualizar_lista()
                    
                    # Cerrar diálogo
                    page.dialog.open = False
                    page.update()
                    
                    # Mostrar mensaje de éxito
                    page.show_snack_bar(
                        ft.SnackBar(
                            content=ft.Text("✅ Reserva actualizada exitosamente", color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.GREEN
                        )
                    )
                    page.update()
                else:
                    page.show_snack_bar(
                        ft.SnackBar(
                            content=ft.Text("❌ Completa todos los campos", color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.RED
                        )
                    )
                    page.update()
            
            def cancelar_edicion(e):
                page.dialog.open = False
                page.update()
            
            # Crear diálogo de edición
            dialog = ft.AlertDialog(
                title=ft.Text("✏️ Editar Reserva"),
                content=ft.Column([edit_nombre, edit_telefono, edit_fecha, edit_hora, edit_personas], width=400, height=300, scroll=ft.ScrollMode.AUTO),
                actions=[
                    ft.TextButton("Cancelar", on_click=cancelar_edicion),
                    ft.ElevatedButton("Guardar Cambios", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE, on_click=guardar_cambios)
                ]
            )
            
            page.dialog = dialog
            dialog.open = True
            page.update()
        
        return on_edit
    
    def actualizar_lista():
        lista_reservas.controls.clear()
        
        if not reservas_list:
            lista_reservas.controls.append(
                ft.Container(
                    content=ft.Text(
                        "📅 No hay reservas registradas",
                        size=16,
                        color=ft.Colors.BLACK,
                        text_align=ft.TextAlign.CENTER
                    ),
                    padding=20,
                    alignment=ft.alignment.center
                )
            )
        else:
            for reserva in reservas_list:
                tarjeta = ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Text(f"👤 {reserva['nombre']}", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_900),
                            ft.Text(f"📞 {reserva['telefono']}", size=14, color=ft.Colors.BROWN_800),
                            ft.Text(f"💬 {reserva['comentarios']}", size=12, color=ft.Colors.BROWN_700)
                        ], expand=True),
                        ft.Column([
                            ft.Text(f"📅 {reserva['fecha']}", size=14, color=ft.Colors.BROWN_800),
                            ft.Text(f"🕐 {reserva['hora']}", size=14, color=ft.Colors.BROWN_800),
                            ft.Text(f"👥 {reserva['personas']} personas", size=14, color=ft.Colors.BROWN_800)
                        ]),
                        ft.Column([
                            ft.Container(
                                content=ft.Text("Confirmada", color=ft.Colors.WHITE, size=12),
                                bgcolor=ft.Colors.GREEN,
                                padding=10,
                                border_radius=15
                            ),
                            ft.Row([
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    icon_color=ft.Colors.BLUE,
                                    tooltip="Editar reserva",
                                    on_click=editar_reserva(reserva)
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE,
                                    icon_color=ft.Colors.RED,
                                    tooltip="Cancelar reserva",
                                    on_click=cancelar_reserva(reserva)
                                )
                            ], spacing=5)
                        ])
                    ]),
                    bgcolor=ft.Colors.BROWN_50,
                    padding=15,
                    border_radius=8,
                    margin=5,
                    border=ft.border.all(1, ft.Colors.BLACK)
                )
                lista_reservas.controls.append(tarjeta)
        
        page.update()
    
    # Header simple
    header = ft.Container(
        content=ft.Row([
            ft.Text(
                "Reservas",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE
            )
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        bgcolor=ft.Colors.BLACK,
        padding=20,
        border_radius=10,
        width=1000
    )
    
    # Campos del formulario - DEFINIDOS GLOBALMENTE
    nombre_field = ft.TextField(
        label="Nombre completo",
        width=250,
        bgcolor=ft.Colors.BROWN_50,
        border_color=ft.Colors.BROWN_700
    )
    
    telefono_field = ft.TextField(
        label="Teléfono",
        width=250,
        bgcolor=ft.Colors.BROWN_50,
        border_color=ft.Colors.BROWN_700
    )
    
    fecha_field = ft.TextField(
        label="Fecha (DD/MM/YYYY)",
        width=250,
        bgcolor=ft.Colors.BROWN_50,
        border_color=ft.Colors.BROWN_700,
        hint_text="01/10/2025"
    )
    
    hora_field = ft.TextField(
        label="Hora (HH:MM)",
        width=250,
        bgcolor=ft.Colors.BROWN_50,
        border_color=ft.Colors.BROWN_700,
        hint_text="20:00"
    )
    
    personas_field = ft.TextField(
        label="Número de personas",
        width=250,
        bgcolor=ft.Colors.BROWN_50,
        border_color=ft.Colors.BROWN_700,
        keyboard_type=ft.KeyboardType.NUMBER
    )
    
    crear_button = ft.ElevatedButton(
        text="🍽️ Crear Reserva",
        width=200,
        height=45,
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        on_click=crear_reserva
    )
    
    # Formulario
    formulario = ft.Container(
        content=ft.Column([
            ft.Text(
                "📝 Nueva Reserva",
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BROWN_900
            ),
            ft.Row([
                ft.Column([nombre_field, telefono_field], spacing=10),
                ft.Column([fecha_field, hora_field], spacing=10),
                ft.Column([personas_field], spacing=10)
            ], spacing=20),
            ft.Container(
                content=crear_button,
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=15)
            )
        ], spacing=15),
        bgcolor=ft.Colors.WHITE,
        padding=20,
        border_radius=10,
        width=1000
    )
    
    # Lista de reservas
    lista_reservas = ft.Column([], spacing=10)
    
    seccion_reservas = ft.Container(
        content=ft.Column([
            ft.Text(
                "📋 Reservas Actuales",
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BROWN_900
            ),
            ft.Container(
                content=ft.Column([lista_reservas], scroll=ft.ScrollMode.AUTO),
                height=300,
                bgcolor=ft.Colors.WHITE,
                border_radius=10,
                padding=10
            )
        ], spacing=10),
        bgcolor=ft.Colors.WHITE,
        padding=20,
        border_radius=10,
        width=1000
    )
    
    # Inicializar la lista
    actualizar_lista()
    
    # Layout principal con scroll
    main_content = ft.Column([
        header,
        ft.Container(height=20),
        formulario,
        ft.Container(height=20),
        seccion_reservas,
        ft.Container(height=50)  # Espacio extra al final
    ], 
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    scroll=ft.ScrollMode.AUTO,
    spacing=0
    )
    
    # Contenedor principal scrolleable
    page.add(
        ft.Container(
            content=main_content,
            expand=True,
            padding=10
        )
    )

if __name__ == "__main__":
    print("🍽️ Iniciando Sistema de Reservas...")
    print("📱 Accede a: http://localhost:8088")
    print("🔄 Para ver cambios: Para servidor (Ctrl+C) y reinicia")
    
    ft.app(
        target=main,
        view=ft.WEB_BROWSER,
        port=8088
    )