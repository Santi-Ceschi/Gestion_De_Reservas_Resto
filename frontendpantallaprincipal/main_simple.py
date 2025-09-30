import flet as ft

def main(page: ft.Page):
        # Configuración de la página
    page.title = "Restaurante Delizioso - Sistema de Reservas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = ft.Colors.WHITE
    page.window_width = 1200
    page.window_height = 800
    page.scroll = ft.ScrollMode.AUTO
    
    # Header
    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Row([
                    ft.Image(
                        src="logo_forja.jpg",
                        width=90,
                        height=120,
                        fit=ft.ImageFit.FILL
                    )
                ]),
                ft.IconButton(
                    icon=ft.Icons.PERSON,
                    icon_color=ft.Colors.WHITE,
                    icon_size=30
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=ft.padding.symmetric(horizontal=50, vertical=20),
        bgcolor=ft.Colors.BLACK,
        height=90
    )
    
    # Variables del carrusel
    carousel_images = [
        "afuera.png",
        "comida.jpeg", 
        "interior.png"
    ]
    current_index = 0
    
    # Crear contenedor de imagen
    image_container = ft.Image(src=carousel_images[current_index], fit=ft.ImageFit.COVER)
    
    # Función para cambiar imagen automáticamente
    def change_image():
        nonlocal current_index
        current_index = (current_index + 1) % len(carousel_images)
        image_container.src = carousel_images[current_index]
        page.update()
    
    # Timer para cambio automático cada 3 segundos
    import asyncio
    async def auto_carousel():
        while True:
            await asyncio.sleep(3)
            change_image()
    
    # Iniciar el carrusel automático
    page.run_task(auto_carousel)
    
    # Contenido principal - Carrusel con overlay
    main_content = ft.Container(
        content=ft.Stack([
            # Imagen de fondo (carrusel)
            image_container,
            # Overlay con texto y botón
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Bienvenido a La Forja",
                        size=48,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Disfruta de la mejor experiencia gastronómica",
                        size=24,
                        color=ft.Colors.WHITE,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=30),  # Espaciado
                    ft.ElevatedButton(
                        "HACER RESERVA",
                        bgcolor=ft.Colors.TRANSPARENT,
                        color=ft.Colors.WHITE,
                        width=200,
                        height=50,
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD)
                        )
                    )
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10),
                alignment=ft.alignment.center,
                # Fondo semitransparente para mejor legibilidad
                bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                padding=40
            )
        ]),
        height=600,
        bgcolor=ft.Colors.WHITE
    )
    
    # Sección con 2 fotos verticales y descripciones al lado
    photo_section = ft.Container(
        content=ft.Column([
            # Primera fila: Foto interior con descripción
            ft.Container(
                content=ft.Row([
                    # Imagen interior con sombra
                    ft.Container(
                        content=ft.Image(
                            src="interior.png",
                            width=400,
                            height=300,
                            fit=ft.ImageFit.COVER
                        ),
                        shadow=ft.BoxShadow(
                            spread_radius=5,
                            blur_radius=15,
                            color=ft.Colors.with_opacity(1, ft.Colors.BLACK),
                            offset=ft.Offset(5, 5)
                        ),
                        border_radius=10
                    ),
                    # Descripción interior
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "Nuestro Ambiente Único",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.GREY_800
                            ),
                            ft.Container(height=15),
                            ft.Text(
                                "Experiencia Gastronómica Excepcional",
                                size=20,
                                weight=ft.FontWeight.W_500,
                                color=ft.Colors.BLACK
                            ),
                            ft.Container(height=20),
                            ft.Text(
                                "Nuestro restaurante ofrece un ambiente acogedor y sofisticado, diseñado meticulosamente para crear la experiencia gastronómica perfecta. Cada rincón ha sido pensado para brindar comodidad y elegancia, desde la iluminación cálida hasta los detalles decorativos que reflejan nuestra pasión por la excelencia culinaria.\n\nDisfruta de un espacio donde la tradición se encuentra con la modernidad, creando el escenario ideal para momentos inolvidables en compañía de tus seres queridos.",
                                size=16,
                                color=ft.Colors.GREY_800,
                                text_align=ft.TextAlign.JUSTIFY
                            )
                        ], spacing=5),
                        padding=40,
                        expand=True
                    )
                ], spacing=30),
                padding=ft.padding.symmetric(horizontal=50, vertical=30)
            ),
            
            # Segunda fila: Foto carne con descripción
            ft.Container(
                content=ft.Row([
                    # Imagen carne con sombra
                    ft.Container(
                        content=ft.Image(
                            src="carne.jpg",
                            width=400,
                            height=300,
                            fit=ft.ImageFit.COVER
                        ),
                        shadow=ft.BoxShadow(
                            spread_radius=5,
                            blur_radius=15,
                            color=ft.Colors.with_opacity(1, ft.Colors.BLACK),
                            offset=ft.Offset(5, 5)
                        ),
                        border_radius=10
                    ),
                    # Descripción carne
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "Nuestra Especialidad Premium",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.GREY_800
                            ),
                            ft.Container(height=15),
                            ft.Text(
                                "Carnes de la Más Alta Calidad",
                                size=20,
                                weight=ft.FontWeight.W_500,
                                color=ft.Colors.BLACK
                            ),
                            ft.Container(height=20),
                            ft.Text(
                                "Seleccionamos cuidadosamente las mejores carnes premium del mercado, trabajando directamente con proveedores de confianza que comparten nuestra filosofía de calidad excepcional. Nuestros chefs expertos preparan cada corte con técnicas tradicionales y modernas, logrando texturas perfectas y sabores únicos.\n\nCada plato es una obra maestra culinaria, donde la pasión por la cocina se combina con ingredientes de primera calidad para ofrecerte una experiencia gastronómica que supera todas las expectativas.",
                                size=16,
                                color=ft.Colors.GREY_800,
                                text_align=ft.TextAlign.JUSTIFY
                            )
                        ], spacing=5),
                        padding=40,
                        expand=True
                    )
                ], spacing=30),
                padding=ft.padding.symmetric(horizontal=50, vertical=30)
            )
        ], spacing=40),
        bgcolor=ft.Colors.WHITE
    )
    
    # Combinar ambas secciones
    main_content = ft.Column([
        main_content,  # El carrusel existente
        photo_section  # La nueva sección de fotos
    ], spacing=0, expand=True)
    
    # Footer
    footer = ft.Container(
        content=ft.Row([
            ft.Column([
                ft.Text("Restaurante Delizioso", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text("© 2025 Todos los derechos reservados", size=12, color=ft.Colors.WHITE70)
            ]),
            ft.Column([
                ft.Text("Contacto", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text("📞 +54 9 3496 56-1006", size=12, color=ft.Colors.WHITE70),
                ft.Text("📧 info@restaurantedelizioso.com", size=12, color=ft.Colors.WHITE70)
            ]),
            ft.Column([
                ft.Text("Ubicación", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text("📍 Ruta Provincial 70 & Tito Bottai", size=12, color=ft.Colors.WHITE70),
                ft.Text("Esperanza, Santa Fe", size=12, color=ft.Colors.WHITE70)
            ])
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
        padding=30,
        bgcolor=ft.Colors.BLACK,
        height=120
    )
    
    # Estructura con footer fijo
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
            # Footer fijo en la parte inferior
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
    ft.app(target=main, view=ft.WEB_BROWSER, port=8083, assets_dir="assets")